from datetime import datetime as dt, timedelta

class Person:
    def __init__(self, day_of_birth, month_of_birth, year_of_birth):
        try:
            self.date_of_birth = dt(year=year_of_birth, month=month_of_birth, day=day_of_birth)
        except ValueError:
            raise ValueError("The date you entered is invalid.")
    
    def calculate_age(self, current_date):
        # Calculate years
        years = current_date.year - self.date_of_birth.year
        if (current_date.month, current_date.day) < (self.date_of_birth.month, self.date_of_birth.day):
            years -= 1
        
        # Calculate months
        months = current_date.month - self.date_of_birth.month
        if current_date.day < self.date_of_birth.day:
            months -= 1
        
        # Adjust month calculation
        if months < 0:
            months += 12
        
        # Calculate days
        if current_date.day >= self.date_of_birth.day:
            days = current_date.day - self.date_of_birth.day
        else:
            # Get the last day of the previous month
            last_day_previous_month = (current_date.replace(day=1) - timedelta(days=1)).day
            days = last_day_previous_month - self.date_of_birth.day + current_date.day
        
        return years, months, days

    def days_since_birth(self, current_date):
        delta_days = (current_date - self.date_of_birth).days
        return delta_days

def input_date_of_birth():
    while True:
        try:
            day_of_birth = int(input('What day were you born: '))
            month_of_birth = int(input('What month were you born: '))
            year_of_birth = int(input('What year were you born: '))
            return Person(day_of_birth, month_of_birth, year_of_birth)
        except ValueError as e:
            print(e)
            print("Please try again.")

# Get a valid date of birth
person = input_date_of_birth()

# Get the current date
current_date = dt.now()

# Calculate the number of days since birth
days_since_birth = person.days_since_birth(current_date)
print(f"Number of days since birth: {days_since_birth} days")

# Calculate age in years, months, and days
age_years, age_months, age_days = person.calculate_age(current_date)
print(f"Your age is: {age_years} years, {age_months} months, and {age_days} days")
