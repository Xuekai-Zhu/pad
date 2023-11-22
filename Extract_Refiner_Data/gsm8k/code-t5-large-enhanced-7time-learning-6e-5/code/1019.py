def solution():
    
    # Define the number of sandwiches eaten per day
    MAN_SANDWICHES_PER_DAY = 5
    WIFE_SANDWICHES_PER_DAY = 4
    SON_SANDWICHES_PER_DAY = 2

    # Calculate the total number of sandwiches eaten in one week
    total_sandwiches_per_week = MAN_SANDWICHES_PER_DAY + WIFE_SANDWICHES_PER_DAY + SON_SANDWICHES_PER_DAY

    # Display the total number of sandwiches eaten in one week
    result = total_sandwiches_per_week
    return result

print(solution())