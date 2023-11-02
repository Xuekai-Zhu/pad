def solution():
    """There are enough provisions in a castle to feed 300 people for 90 days. After 30 days, 100 people leave the castle. How many more days are left until all the food runs out?"""
    # Define the initial number of people and days
    initial_people = 300
    initial_days = 90

    # Calculate the initial amount of food
    initial_food = initial_people * initial_days

    # Calculate the remaining number of people and days
    remaining_people = initial_people - 100
    remaining_days = initial_days - 30

    # Calculate the remaining amount of food
    remaining_food = remaining_people * remaining_days

    # Calculate the number of days until all the food runs out
    days_left = remaining_food / (initial_food / initial_days)

    result = days_left
    return result

print(solution())