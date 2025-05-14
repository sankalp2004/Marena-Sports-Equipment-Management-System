import os
import django
import csv

# Set the DJANGO_SETTINGS_MODULE environment variable
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SportsEquipment.settings")

# Initialize Django
django.setup()

from goods.models import Goods  # Import your model after initializing Django

# Assuming the CSV file is in the 'data' directory
csv_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data', 'available_goods.csv')

with open(csv_file_path, 'r') as file:
    reader = csv.DictReader(file)

    for row in reader:
        # Convert boolean values from strings to actual booleans
        row['issued'] = row['issued'].lower() == 'true'

        # Use get_or_create to insert or update the data in the database
        obj, created = Goods.objects.get_or_create(defaults=row, **{k: row[k] for k in row if k != 'item_id'}, id=row['item_id'])

        if not created:
            # If the object already exists, update its fields
            for key, value in row.items():
                setattr(obj, key, value)

            # Save the updated object to the database
            obj.save()