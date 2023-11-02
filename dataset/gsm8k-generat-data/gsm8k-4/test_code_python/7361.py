def solution():
    """John works at 2 different hospitals. At the first hospital, he sees 20 different patients each day. At the second hospital, he sees 20% more individual patients a day. He works 5 days a week. How many patients does he treat a year if he works 50 weeks a year?"""
    # Define the number of patients John sees at the first hospital each week
    hospital_1_patients_per_week = 20

    # Calculate the number of patients John sees at the second hospital each week, accounting for the 20% increase
    hospital_2_patients_per_week = hospital_1_patients_per_week * 1.2

    # Calculate the total number of patients John sees each week
    total_patients_per_week = hospital_1_patients_per_week + hospital_2_patients_per_week

    # Calculate the total number of patients John sees in a year
    total_patients_per_year = total_patients_per_week * 5 * 50

    # return the result
    result = total_patients_per_year
    return result

print(solution())