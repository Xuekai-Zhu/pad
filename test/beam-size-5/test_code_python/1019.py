def solution():
    
    # Define the number of sandwiches eaten by each family member per day
    MAN_SANDWICHES = 5
    WIFE_SANDWICHES = 4
    SON_SANDWICHES = 2

    # Define the number of days in a week
    DAYS_IN_WEEK = 7

    # Calculate the total number of sandwiches eaten by the family in a week
    total_sandwiches = (MAN_SANDWICHES + WIFE_SANDWICHES + SON_SANDWICHES) * DAYS_IN_WEEK

    # Display the total number of sandwiches eaten
    result = total_sandwiches
    return result

print(solution())