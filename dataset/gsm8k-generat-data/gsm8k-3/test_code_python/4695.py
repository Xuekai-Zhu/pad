def solution():
    """Nancy takes 3 antacids per day when she eats Indian food, 2 antacids per day when she eats Mexican food, and 1 antacid per day otherwise. If Nancy eats Indian three times a week and Mexican twice a week, how many antacids does she take per month?"""
    # Define the number of days and weeks in a month
    DAYS_IN_MONTH = 30
    WEEKS_IN_MONTH = 4

    # Define the number of antacids Nancy takes per day for different types of food
    ANTACIDS_FOR_INDIAN = 3
    ANTACIDS_FOR_MEXICAN = 2
    ANTACIDS_FOR_OTHER = 1

    # Define the number of times Nancy eats Indian and Mexican food in a month
    indian_frequency = 3
    mexican_frequency = 2

    # Calculate the total number of antacids Nancy takes in a month
    total_antacids = (indian_frequency * ANTACIDS_FOR_INDIAN + mexican_frequency * ANTACIDS_FOR_MEXICAN 
                      + (DAYS_IN_MONTH - (indian_frequency + mexican_frequency) * 7) * ANTACIDS_FOR_OTHER) * WEEKS_IN_MONTH

    # Display the total number of antacids Nancy takes per month
    result = total_antacids
    return result

print(solution())