import pandas as pd

def calculate_demographic_data(print_data=True):
    df = pd.read_csv('/Users/stefanoparente/Desktop/Ponderada_Curso/demographic_data_analyzer/adult.data.csv')

    race_count = df['race'].value_counts()
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)
    percentage_bachelors = round((df['education'].value_counts().get('Bachelors', 0) / len(df)) * 100, 1)
    advanced_education = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    percentage_advanced_education_50k = round((advanced_education[advanced_education['salary'] == '>50K'].shape[0] /
                                               advanced_education.shape[0]) * 100, 1) if advanced_education.shape[0] > 0 else 0
    non_advanced_education = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    percentage_non_advanced_education_50k = round((non_advanced_education[non_advanced_education['salary'] == '>50K'].shape[0] /
                                                   non_advanced_education.shape[0]) * 100, 1) if non_advanced_education.shape[0] > 0 else 0
    min_hours_per_week = df['hours-per-week'].min()
    min_hours_workers = df[df['hours-per-week'] == min_hours_per_week]
    percentage_min_hours_50k = round((min_hours_workers[min_hours_workers['salary'] == '>50K'].shape[0] /
                                      min_hours_workers.shape[0]) * 100, 1) if min_hours_workers.shape[0] > 0 else 0
    countries = df[df['salary'] == '>50K']['native-country'].value_counts()
    countries_total = df['native-country'].value_counts()
    highest_percentage_country = ((countries / countries_total) * 100).idxmax() if not countries.empty else None
    highest_percentage = round(((countries / countries_total) * 100).max(), 1) if not countries.empty else None
    india_occupations = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]['occupation']
    most_popular_occupation_india = india_occupations.value_counts().idxmax() if not india_occupations.empty else None

    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with advanced education that earn >50K: {percentage_advanced_education_50k}%")
        print(f"Percentage without advanced education that earn >50K: {percentage_non_advanced_education_50k}%")
        print(f"Minimum hours worked per week: {min_hours_per_week}")
        print(f"Percentage of rich among those who work fewest hours: {percentage_min_hours_50k}%")
        print(f"Country with highest percentage of rich: {highest_percentage_country} ({highest_percentage}%)")
        print(f"Top occupation in India: {most_popular_occupation_india}")

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'percentage_advanced_education_50k': percentage_advanced_education_50k,
        'percentage_non_advanced_education_50k': percentage_non_advanced_education_50k,
        'min_hours_per_week': min_hours_per_week,
        'percentage_min_hours_50k': percentage_min_hours_50k,
        'highest_percentage_country': highest_percentage_country,
        'highest_percentage': highest_percentage,
        'most_popular_occupation_india': most_popular_occupation_india
    }
