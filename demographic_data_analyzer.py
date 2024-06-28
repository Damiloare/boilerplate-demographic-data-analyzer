import pandas as pd


def calculate_demographic_data(print_data=True):
    df = pd.read_csv('adult_data.csv')
    df
    #Output the columns in the dataset for proper reference in the codes
    print(df.columns)
    #display the first five rows of dataset
    df.head(5)
    #How many people of each race are represented in this dataset? 
    race_total = df.race.value_counts()
    race_total
    
    #What is the average age of men?
    AVG = df[df.sex == "Male"].age.mean()
    ave_age_men = round(AVG,4)
    print("Average Age Of Men =  ", ave_age_men)
    
    #What is the percentage of people with different Qualifications?
    diff_Qualifications = (df.education.value_counts(normalize = True)*100 )
    qualifications = round(diff_Qualifications, 4) 
    print ('Percentage of Different Qualifications: ', qualifications)
    
    #What is the percentage of people who have a Bachelor's degree
    per_Bachelors = ((df.education.value_counts(normalize = True).Bachelors)*100)
    percent_Bachelors = round(per_Bachelors,2)
    print('Percentage of people with Bachelors Degree: ', percent_Bachelors,'%')
    advanced_education = df.loc[df["education"].isin(["Bachelors", "Masters", "Doctorate"])]
    print('Table list of people with advanced education: ')
    advanced_education
    
    #What percentage of people with advanced education (Bachelors, Masters, or Doctorate) make more than 50K?
    #Note: 'salary' attribute is identified as 'class' in the dataset
    rich_advanced_education = round((advanced_education.loc[advanced_education["class"] == ">50K"].size)*100
        / advanced_education.size,2)
    print('Percentage of people with advanced education that earn above 50k:', rich_advanced_education, '%')
    lower_Education = df.loc[~df["education"].isin(["Bachelors", "Masters", "Doctorate"])]
    print('Table list of people with lower education: ')
    lower_Education
    
    #What percentage of people without advanced education make more than 50K?
    rich_Lower_Education = round((lower_Education.loc[lower_Education['class'] == '>50k'].size) * 100/ lower_Education.size, 2)
    print('Percentage of people with lower education that earn above 50k:', rich_Lower_Education,'%')
    
    #What is the minimum number of hours a person works per week?
    min_Hours_Per_Week = df['hoursperweek'].min()
    print('Minimum hours worked per a week: ', min_Hours_Per_Week, 'hours/week')
    
    #What percentage of the people who work the minimum number of hours per week have a salary of more than 50K?
    num_min_workers = df.loc[df["hoursperweek"] == min_Hours_Per_Week]
    rich_percentage_NMW = round((num_min_workers.loc[num_min_workers["class"] == 
                                                  ">50K"].size) *100/ num_min_workers.size,2)
    print ("Percentage of people who work minimum numbers of hours per week but earn above 50k:", 
       rich_percentage_NMW,'%')
    #Countries and their earnings
    countries_earnings = (df[["class", "native-country"]].groupby("native-country")
        .apply(lambda g: g.loc[g["class"] == ">50K"].size / g.size * 100))
    print('Summation of earnings by countries:')
    countries_earnings
    
    #What country has the highest percentage of people that earn >50K and what is that percentage?
    highest_Earning_Country =countries_earnings.idxmax()
    highest_earning_country_percentage = round(countries_earnings.max(),2)
    print('Highest Earning Country:', highest_Earning_Country)
    print('Percentage of highest earning country:',highest_earning_country_percentage,"%")
    
    #Identify the most popular occupation for those who earn >50K in India.
    most_popular_occupation = (df.loc[(df["native-country"] == "India") & (df["class"] == ">50K")]
                           ["occupation"].value_counts().idxmax())
    print('Most Popular Occupation in India:', most_popular_occupation)

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
