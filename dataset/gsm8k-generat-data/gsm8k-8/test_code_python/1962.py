def solution():
    # Define the number of paintings Philip makes in one day
    paintings_per_day = 2

    # Define the starting number of paintings
    starting_paintings = 20

    # Define the number of days
    days = 30

    # Calculate the total number of paintings after 30 days
    total_paintings = starting_paintings + (paintings_per_day * days)
    result = total_paintings
    return result

print(solution())