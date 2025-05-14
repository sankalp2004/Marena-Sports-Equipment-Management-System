
# goods/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from .models import Goods, IssuedGoods, StudentLog
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
import pytz
import csv
import os
from io import StringIO
from django.contrib.auth import authenticate, login
from django.contrib import messages



def admin_login(request):
    # Your admin login view logic here
    return render(request, 'goods/admin_login.html')

def maintenance_login(request):
    # Your maintenance login view logic here
    return render(request, 'goods/maintenance_login.html')

def landing_page(request):
    return render(request, 'goods/landing_page.html')

def dashboard(request):
    return render(request, 'goods/dashboard.html')

def goods_list(request):
    csv_file_path = 'data/available_goods.csv'

    # Read CSV data for available goods
    with open(csv_file_path, 'r') as file:
        reader = csv.DictReader(file)
        goods_data = list(reader)

    context = {'goods': goods_data}
    return render(request, 'goods/goods_list.html', context)

def issued_goods_list(request):
    issued_goods_csv_path = 'data/issued_goods.csv'
    with open(issued_goods_csv_path, 'r') as file:
        reader = csv.DictReader(file)
        goods_data = list(reader)

    context = {'issued_goods': goods_data}
    return render(request, 'goods/issued_goods_list.html', context)

def student_logs_list(request):
    student_log_csv_path = 'data/student_logs.csv'
    with open(student_log_csv_path, 'r') as file:
        reader = csv.DictReader(file)
        goods_data = list(reader)

    context = {'student_logs': goods_data}
    return render(request, 'goods/student_logs_list.html', context)


class MyLoginView(LoginView):
    success_url = reverse_lazy('dashboard')
    

def issue_equipment(request):
    csv_file_path = 'data/available_goods.csv'
    issued_goods_csv_path = 'data/issued_goods.csv'
    student_log_csv_path = 'data/student_logs.csv'

    # Read CSV data for available goods
    with open(csv_file_path, 'r') as file:
        reader = csv.DictReader(file)
        goods_data = list(reader)

    context = {'goods_items': goods_data}
    
    if request.method == 'POST':
        # Retrieve form data
        equipment = int(request.POST.get('equipment'))
        item_name = request.POST.get('item_name')
        name = request.POST.get('name')
        department = request.POST.get('department')
        regno = request.POST.get('registration_number')
        phoneno = request.POST.get('phone_number')
        quantity = int(request.POST.get('quantity'))

        # Check if regno is already in issued goods
        with open(issued_goods_csv_path, 'r') as issued_file:
            issued_reader = csv.DictReader(issued_file)
            for issued_item in issued_reader:
                if issued_item['regno'] == regno:
                    # If regno is already in issued goods, redirect to error page
                    messages.error(request, 'Equipment already issued to the student with the provided registration number.')
                    return redirect('error')

        # Find the item in the CSV data
        for item in goods_data:
            if int(item['item_id']) == equipment and int(item['available_quantity']) >= quantity:
                # Update available quantity in memory
                item['available_quantity'] = str(int(item['available_quantity']) - quantity)
                # Convert current datetime to IST
                ist = pytz.timezone('Asia/Kolkata')  # Adjust timezone according to your location
                current_datetime_ist = timezone.now().astimezone(ist)
                # Write data to the CSV file
                with open(csv_file_path, 'w', newline='') as goods_file:
                    fieldnames = ['item_id', 'item_name', 'total_quantity', 'available_quantity', 'issued']
                    writer = csv.DictWriter(goods_file, fieldnames=fieldnames)
                    writer.writeheader()
                    writer.writerows(goods_data)

                # Write data to the issued goods CSV file
                with open(issued_goods_csv_path, 'a', newline='') as issued_goods_file:
                    fieldnames = ['item_id', 'item_name', 'name', 'department', 'regno', 'phoneno', 'no_issued', 'date_of_issue', 'time_of_issue']
                    issued_goods_writer = csv.DictWriter(issued_goods_file, fieldnames=fieldnames)
                    issued_goods_writer.writerow({
                        'item_id': equipment,
                        'item_name': item['item_name'],
                        'name': name,
                        'department': department,
                        'regno': regno,
                        'phoneno': phoneno,
                        'no_issued': quantity,
                        'date_of_issue': current_datetime_ist.date(),
                        'time_of_issue': current_datetime_ist.time(),
                    })

                # Write data to the student log CSV file
                with open(student_log_csv_path, 'a', newline='') as student_log_file:
                    fieldnames = ['item_id', 'item_name', 'name', 'department', 'regno', 'phoneno', 'no_issued', 'date_of_issue', 'time_of_issue']
                    student_log_writer = csv.DictWriter(student_log_file, fieldnames=fieldnames)
                    student_log_writer.writerow({
                        'item_id': equipment,
                        'item_name': item['item_name'],
                        'name': name,
                        'department': department,
                        'regno': regno,
                        'phoneno': phoneno,
                        'no_issued': quantity,
                        'date_of_issue': current_datetime_ist.date(),
                        'time_of_issue': current_datetime_ist.time(),
                    })

                print("reached redirect to viewing")
                return redirect('view_issued_goods')  # Redirect to a success page or the same page

        # Handle cases where goods with the given ID do not exist or quantity is insufficient
        print("Entered else")
        return redirect('error')  

    # Render the form for GET requests
    return render(request, 'goods/issue_equipment.html', context)

def return_equipment(request):
    csv_file_path = 'data/available_goods.csv'
    issued_goods_csv_path = 'data/issued_goods.csv'
    student_log_csv_path = 'data/student_logs.csv'

    # Read CSV data for issued goods
    with open(issued_goods_csv_path, 'r') as file:
        reader = csv.DictReader(file)
        issued_goods_data = list(reader)

    context = {'issued_goods': issued_goods_data}

    if request.method == 'POST':
        # Retrieve form data
        regno = request.POST.get('registration_number')
        penalty = int(request.POST.get('penalty'))

        # Specify the path to your CSV files
        issued_goods_csv_path = 'data/issued_goods.csv'
        student_log_csv_path = 'data/student_logs.csv'
        available_goods_csv_path = 'data/available_goods.csv'

        # Read CSV data for issued goods
        with open(issued_goods_csv_path, 'r') as issued_goods_file:
            issued_goods_reader = csv.DictReader(issued_goods_file)
            issued_goods_data = list(issued_goods_reader)

        # Find the item in the issued goods CSV data
        for item in issued_goods_data:

            print(regno)
            print(item)

            if item['regno'] == regno:
                # Convert current datetime to IST
                ist = pytz.timezone('Asia/Kolkata')  # Adjust timezone according to your location
                current_datetime_ist = timezone.now().astimezone(ist)

                # Update return details in the student log CSV file
                with open(student_log_csv_path, 'a', newline='') as student_log_file:
                    fieldnames = ['item_id', 'item_name', 'name', 'department', 'regno', 'phoneno', 'no_issued', 'date_of_issue', 'time_of_issue', 'returned', 'return_date', 'return_time', 'penalty']
                    student_log_writer = csv.DictWriter(student_log_file, fieldnames=fieldnames)
                    student_log_writer.writerow({
                        'item_id': item['item_id'],
                        'item_name': item['item_name'],
                        'name': item['name'],
                        'department': item['department'],
                        'regno': item['regno'],
                        'phoneno': item['phoneno'],
                        'no_issued': item['no_issued'],
                        'date_of_issue': item['date_of_issue'],
                        'time_of_issue': item['time_of_issue'],
                        'returned': 'True',
                        'return_date': current_datetime_ist.date(),
                        'return_time': current_datetime_ist.time(),
                        'penalty': penalty,
                    })

                # Update available quantity in the available goods CSV file
                with open(available_goods_csv_path, 'r') as available_goods_file:
                    available_goods_reader = csv.DictReader(available_goods_file)
                    available_goods_data = list(available_goods_reader)

                for available_item in available_goods_data:
                    if available_item['item_id'] == item['item_id']:
                        available_item['available_quantity'] = str(int(available_item['available_quantity']) + int(item['no_issued']))

                with open(available_goods_csv_path, 'w', newline='') as available_goods_file:
                    fieldnames = ['item_id', 'item_name', 'total_quantity', 'available_quantity', 'issued']
                    available_goods_writer = csv.DictWriter(available_goods_file, fieldnames=fieldnames)
                    available_goods_writer.writeheader()
                    available_goods_writer.writerows(available_goods_data)

                # Remove the returned item from the issued goods CSV file
                issued_goods_data.remove(item)

                with open(issued_goods_csv_path, 'w', newline='') as issued_goods_file:
                    fieldnames = ['item_id', 'item_name', 'name', 'department', 'regno', 'phoneno', 'no_issued', 'date_of_issue', 'time_of_issue']
                    issued_goods_writer = csv.DictWriter(issued_goods_file, fieldnames=fieldnames)
                    issued_goods_writer.writeheader()
                    issued_goods_writer.writerows(issued_goods_data)

                print("reached redirect to return success")
                return redirect('view_student_logs')  # Redirect to a success page

    # Render the form for GET requests
    return render(request, 'goods/return_equipment.html', context)

class AdminLoginView(LoginView):
    template_name = 'goods/admin_login.html'
    success_url = '/goods/dashboard/'

    def post(self, request, *args, **kwargs):
        username = request.POST.get('uname')
        password = request.POST.get('psw')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect(self.success_url)
        else:
            messages.error(request, 'Incorrect username or password, please try again.')
            return render(request, self.template_name, {})

class MyLoginView(LoginView):
    success_url = reverse_lazy('dashboard')

class MaintenanceLoginView(LoginView):
    template_name = 'goods/maintenance_login.html'
    success_url = '/goods/dashboard/'  # Change this to the appropriate URL

    def post(self, request):
        username = request.POST.get('uname')
        password = request.POST.get('psw')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect(self.success_url)
        else:
            messages.error(request, 'Incorrect username or password')
            return render(request, self.template_name, {})

