import pandas as pd

# Load the dataset
df = pd.read_csv('census_data.csv')

# 1. How many people of each race are represented in this dataset?
def race_count():
    return df['race'].value_counts()

# 2. What is the average age of men?
def average_age_men():
    return round(df[df['sex'] == 'Male']['age'].mean(), 1)

# 3. What is the percentage of people who have a Bachelor's degree?
def percentage_bachelors():
    bachelors = df[df['education'] == 'Bachelors']
    return round((len(bachelors) / len(df)) * 100, 1)

# 4. What percentage of people with advanced education (Bachelors, Masters, or Doctorate) make more than 50K?
def percentage_higher_education_salary():
    advanced_education = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    return round((len(advanced_education[advanced_education['salary'] == '>50K']) / len(advanced_education)) * 100, 1)

# 5. What percentage of people without advanced education make more than 50K?
def percentage_no_higher_education_salary():
    no_advanced_education = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    return round((len(no_advanced_education[no_advanced_education['salary'] == '>50K']) / len(no_advanced_education)) * 100, 1)

# 6. What is the minimum number of hours a person works per week?
def min_work_hours():
    return df['hours-per-week'].min()

# 7. What percentage of the people who work the minimum number of hours per week have a salary of more than 50K?
def percentage_min_work_hours_salary():
    min_hours = df['hours-per-week'].min()
    min_hours_workers = df[df['hours-per-week'] == min_hours]
    return round((len(min_hours_workers[min_hours_workers['salary'] == '>50K']) / len(min_hours_workers)) * 100, 1)

# 8. What country has the highest percentage of people that earn >50K and what is that percentage?
def highest_earning_country():
    countries = df['native-country'].unique()
    country_percentages = {}
    
    for country in countries:
        country_data = df[df['native-country'] == country]
        earners = len(country_data[country_data['salary'] == '>50K'])
        total = len(country_data)
        country_percentages[country] = round((earners / total) * 100, 1)

    highest_earning = max(country_percentages, key=country_percentages.get)
    return highest_earning, country_percentages[highest_earning]

# 9. Identify the most popular occupation for those who earn >50K in India.
def top_occupation_in_india():
    india_data = df[df['native-country'] == 'India']
    high_income_india = india_data[india_data['salary'] == '>50K']
    return high_income_india['occupation'].mode()[0]

