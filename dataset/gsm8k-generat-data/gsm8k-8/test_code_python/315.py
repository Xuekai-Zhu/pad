def solution():
    # Define the initial number of people and days
    initial_people = 300
    initial_days = 90

    # Calculate the initial amount of food needed
    initial_food = initial_people * initial_days

    # Calculate the remaining amount of food after 30 days with 200 people
    remaining_people = 200
    remaining_days = initial_days - 30
    remaining_food = remaining_people * remaining_days

    # Calculate the number of days until all the food runs out
    days_left = remaining_food / (initial_food / initial_days)
    result = days_left
    return result

print(solution())