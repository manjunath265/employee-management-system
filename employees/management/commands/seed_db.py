import random
from datetime import date, timedelta
from django.core.management.base import BaseCommand
from departments.models import Department
from employees.models import Employee
from attendance.models import Attendance
from performance.models import Performance

from faker import Faker

fake = Faker()

DEPARTMENTS = ['Engineering', 'HR', 'Marketing', 'Sales', 'Finance', 'IT']

STATUS_CHOICES = ['present', 'absent', 'late']

class Command(BaseCommand):
    help = 'Seeds the database with sample data'

    def handle(self, *args, **kwargs):
        self.stdout.write("Seeding data...")

        # Create Departments
        departments = []
        for name in DEPARTMENTS:
            dept, created = Department.objects.get_or_create(name=name)
            departments.append(dept)

        # Create Employees
        for _ in range(50):
            dept = random.choice(departments)
            Employee.objects.get_or_create(
                name=fake.name(),
                email=fake.email(),
                phone=fake.phone_number(),
                address=fake.address(),
                department=dept
            )

        # Create Attendance records for last 30 days
        employees = Employee.objects.all()
        today = date.today()
        start_date = today - timedelta(days=30)

        for employee in employees:
            current_date = start_date
            while current_date <= today:
                if current_date.weekday() < 5:  # Skip weekends
                    Attendance.objects.get_or_create(
                        employee=employee,
                        date=current_date,
                        status=random.choice(STATUS_CHOICES)
                    )
                current_date += timedelta(days=1)

        # Create Performance reviews
        for employee in employees:
            Performance.objects.get_or_create(
                employee=employee,
                rating=random.randint(1, 5),
                review_date=fake.date_between(start_date='-1y', end_date='today')
            )

        self.stdout.write(self.style.SUCCESS("Successfully seeded the database."))