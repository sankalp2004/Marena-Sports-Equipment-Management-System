# Marena Sports Equipment Management System

A comprehensive sports equipment organization website developed for Manipal Institute of Technology Bengaluru. This web application streamlines sports equipment inventory management with real-time database operations and Excel export functionality.

## Project Overview

The Marena Sports Equipment Management System is a full-stack Django web application designed specifically for MIT Bengaluru's sports department. It provides efficient equipment tracking, real-time database updates, and comprehensive data export capabilities.

## Technology Stack

- **Backend**: Python
- **Framework**: Django
- **Frontend**: HTML, CSS
- **Database**: SQLite/PostgreSQL (Django ORM)
- **Export Format**: Excel (.xlsx)

## Key Features

### Real-time Database Operations
- **Instant Updates**: Every functional interaction immediately updates the database
- **Live Data Sync**: All equipment changes are reflected in real-time
- **Seamless Integration**: Backend and frontend work in perfect harmony

### Database Export Functionality
- **Excel Download**: Click "Download Database" to export selected database records
- **Customizable Export**: Choose specific database tables or records to download
- **Formatted Output**: Clean, organized Excel files for easy data analysis

### Equipment Management
- Add new sports equipment to inventory
- Update equipment status and availability
- Track equipment usage and maintenance
- Monitor equipment allocation and returns

### Institution-Specific Features
- Tailored for MIT Bengaluru's sports department requirements
- User-friendly interface for staff and administrators
- Comprehensive equipment categorization

## Installation & Setup

### Prerequisites
- Python 3.8+
- Django 3.2+
- pip package manager

### Installation Steps

1. Clone the repository
    git clone https://github.com/sankalp2004/Marena-Sports-Equipment-Management-System.git

2. Navigate to project directory
    cd Marena-Sports-Equipment-Management-System

3. Create virtual environment
    python -m venv venv

4. Activate virtual environment
    Windows:
    venv\Scripts\activate

    macOS/Linux:
    source venv/bin/activate

5. Install dependencies
    pip install -r requirements.txt

6. Run database migrations
    python manage.py makemigrations
    python manage.py migrate

7. Create superuser (optional)
    python manage.py createsuperuser

Start the development server
python manage.py runserver


## Usage Guide

### Equipment Management
1. **Add Equipment**: Use the equipment form to add new sports items
2. **Update Status**: Click on any equipment to modify its details
3. **Track Inventory**: Monitor equipment availability in real-time

### Database Operations
1. **Real-time Updates**: Every button click or form submission updates the database instantly
2. **Data Export**: 
   - Navigate to the database section
   - Select the records you want to export
   - Click "Download Database" button
   - Excel file will be automatically downloaded

### Key Functional Features
- **Equipment Registration**: Add new equipment with details
- **Status Updates**: Modify equipment availability and condition
- **User Management**: Handle equipment assignments and returns
- **Reporting**: Generate and download comprehensive reports

## Institution Integration

- **Developed for**: Manipal Institute of Technology Bengaluru
- **Department**: Sports Department
- **Purpose**: Streamline sports equipment organization and tracking
- **Users**: Sports staff, administrators, and equipment managers

## Project Structure

Marena-Sports-Equipment-Management-System/
├── manage.py
├── requirements.txt
├── marena/
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
├── equipment/
│ ├── models.py
│ ├── views.py
│ ├── urls.py
│ ├── forms.py
│ └── templates/
│ └── equipment/
├── static/
│ ├── css/
│ ├── js/
│ └── images/
└── media/
└── exports/


## Core Functionality

### Database Integration
- **Django ORM**: Efficient database operations
- **Real-time Updates**: Immediate reflection of all changes
- **Data Integrity**: Consistent and reliable data management

### Export System
- **Excel Generation**: Automated Excel file creation
- **Selective Export**: Choose specific data sets for download
- **Formatted Reports**: Professional-looking exported files

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/NewFeature`)
3. Commit your changes (`git commit -m 'Add NewFeature'`)
4. Push to the branch (`git push origin feature/NewFeature`)
5. Open a Pull Request

## Requirements

Django>=3.2.0
openpyxl>=3.0.0
pandas>=1.3.0
python-decouple>=3.4
Pillow>=8.0.0


## Future Enhancements

- Mobile responsive design
- Advanced search and filtering
- Equipment maintenance scheduling
- User authentication and role management
- Real-time notifications
- Equipment booking system
- Analytics dashboard

## Support

For any queries or support related to this project, please contact the development team or raise an issue in the repository.

## Developer

**Sankalp** - [GitHub Profile](https://github.com/sankalp2004)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
