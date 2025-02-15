import pandas as pd

def demographic_data_analyzer():
    # Load the dataset
    df = pd.read_csv("adult.data.csv")
    
    # Number of people of each race
    race_count = df['race'].value_counts()
    
    # Average age of men
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)
    
    # Percentage of people with a Bachelor's degree
    percentage_bachelors = round((df['education'] == 'Bachelors').mean() * 100, 1)
    
    # Higher education filter
    higher_education = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    
    # Percentage of people with advanced education making more than 50K
    higher_education_rich = round((df[higher_education]['salary'] == '>50K').mean() * 100, 1)
    
    # Percentage of people without advanced education making more than 50K
    lower_education_rich = round((df[~higher_education]['salary'] == '>50K').mean() * 100, 1)
    
    # Minimum hours worked per week
    min_hours_per_week = df['hours-per-week'].min()
    
    # Percentage of people working the minimum hours per week earning >50K
    min_workers = df[df['hours-per-week'] == min_hours_per_week]
    rich_percentage = round((min_workers['salary'] == '>50K').mean() * 100, 1)
    
    # Country with highest percentage of people earning >50K
    rich_by_country = df[df['salary'] == '>50K']['native-country'].value_counts() / df['native-country'].value_counts() * 100
    highest_earning_country = rich_by_country.idxmax()
    highest_earning_country_percentage = round(rich_by_country.max(), 1)
    
    # Most popular occupation for those who earn >50K in India
    india_high_earners = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
    top_IN_occupation = india_high_earners['occupation'].value_counts().idxmax()
    
    # Return the results
    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_hours_per_week': min_hours_per_week,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }

# Running the function
if __name__ == "__main__":
    results = demographic_data_analyzer()
    for key, value in results.items():
        print(f"{key}: {value}")
