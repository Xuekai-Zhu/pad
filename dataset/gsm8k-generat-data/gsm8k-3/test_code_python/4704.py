def solution():
    """John visits three different countries. He stays in the first country for 2 weeks and he spends twice as long in each of the other two countries. How much time does he spend on the trip?"""
    # Define the variables
    first_country_weeks = 2
    second_country_weeks = first_country_weeks * 2
    third_country_weeks = second_country_weeks * 2

    # Calculate the total time John spent on the trip
    total_weeks = first_country_weeks + second_country_weeks + third_country_weeks
    total_time = total_weeks * 7   # converting weeks to days

    # Display the total time
    result = total_time
    return result

print(solution())