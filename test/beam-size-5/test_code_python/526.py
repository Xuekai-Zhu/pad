def solution():
    
    # Define the number of weeks and the number of hours spent on occasions
    num_weeks = 8
    num_hours_occasions = 4

    # Calculate the total number of hours spent on occasions
    total_hours_occasions = num_weeks - num_occasions

    # Calculate the total number of hours spent on the first two weeks
    total_hours_first_two_weeks = 5 * 2 * num_hours_occasions

    # Calculate the total number of hours spent on the second week
    total_hours_second_week = 6 * 1

    # Calculate the total number of hours spent working out across the 8 weeks
    total_hours = total_hours_first_two_weeks + total_hours_second_week

    # return the result
    result = total_hours
    return result

print(solution())