from datetime import datetime as dt, timedelta

class Person:
    def __init__(self, day_born, month_born, year_born):
        try:
            self.date_born = dt(year=year_born, month=month_born, day=day_born)
        except ValueError:
            raise ValueError("Tanggal yang Anda masukkan tidak valid.")
    
    def calculate_age(self, current_date):
        # Calculate years
        years = current_date.year - self.date_born.year
        if (current_date.month, current_date.day) < (self.date_born.month, self.date_born.day):
            years -= 1
        
        # Calculate months
        months = current_date.month - self.date_born.month
        if current_date.day < self.date_born.day:
            months -= 1
        
        # Adjust month calculation
        if months < 0:
            months += 12
        
        # Calculate days
        if current_date.day >= self.date_born.day:
            days = current_date.day - self.date_born.day
        else:
            # Get the last day of the previous month
            last_day_previous_month = (current_date.replace(day=1) - timedelta(days=1)).day
            days = last_day_previous_month - self.date_born.day + current_date.day
        
        return years, months, days

    def days_since_birth(self, current_date):
        delta_days = (current_date - self.date_born).days
        return delta_days

def input_tanggal_lahir():
    while True:
        try:
            day_born = int(input('Tanggal berapa kamu lahir: '))
            month_born = int(input('Bulan apa kamu lahir: '))
            year_born = int(input('Tahun berapa kamu lahir: '))
            return Person(day_born, month_born, year_born)
        except ValueError as e:
            print(e)
            print("Silakan coba lagi.")

# Mendapatkan tanggal lahir yang valid
person = input_tanggal_lahir()

# Mendapatkan tanggal saat ini
date_now = dt.now()

# Menghitung selisih hari
delta_days = person.days_since_birth(date_now)
print(f"Jumlah hari sejak tanggal lahir: {delta_days} hari")

# Menghitung umur dalam tahun, bulan, dan hari
age_years, age_months, age_days = person.calculate_age(date_now)
print(f"Umur kamu: {age_years} tahun, {age_months} bulan, dan {age_days} hari")
