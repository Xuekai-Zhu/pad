def solution():
    """Tricia buys large bottles of iced coffee that have 6 servings per container. She drinks half a container a day. The coffee is currently on sale for $3.00 a bottle. How much will it cost her to buy enough bottles to last for 2 weeks?"""
    # Define the number of servings Tricia drinks per day and the number of days in 2 weeks
    servings_per_day = 3
    days = 14

    # Calculate the total number of servings Tricia will need for 2 weeks
    total_servings = servings_per_day * days

    # Calculate the total number of bottles Tricia will need
    total_bottles = total_servings / 6

    # Calculate the total cost of the coffee
    total_cost = total_bottles * 3

    result = total_cost
    return result

print(solution())