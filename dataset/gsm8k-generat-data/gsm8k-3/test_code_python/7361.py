def solution():
    """John works at 2 different hospitals.  At the first hospital, he sees 20 different patients each day.  At the second hospital, he sees 20% more individual patients a day.  He works 5 days a week.  How many patients does he treat a year if he works 50 weeks a year?"""
    # Define the number of patients John sees at the first hospital
    hospital1_patients_per_day = 20

    # Define the percentage increase in patients the second hospital has
    hospital2_percent_increase = 20

    # Calculate the number of patients John sees at the second hospital
    hospital2_patients_per_day = hospital1_patients_per_day + (hospital1_patients_per_day * hospital2_percent_increase / 100)

    # Calculate the total number of patients John sees each day
    total_patients_per_day = hospital1_patients_per_day + hospital2_patients_per_day

    # Calculate the total number of patients John sees each week
    total_patients_per_week = total_patients_per_day * 5

    # Calculate the total number of patients John sees in a year
    total_patients_per_year = total_patients_per_week * 50

    # Display the total number of patients
    result = total_patients_per_year
    return result

print(solution())