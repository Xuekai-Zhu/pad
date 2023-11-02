def solution():
    """Tricia buys large bottles of iced coffee that have 6 servings per container.  She drinks half a container a day.  The coffee is currently on sale for $3.00 a bottle.  How much will it cost her to buy enough bottles to last for 2 weeks?"""
    # Determine the number of servings Tricia drinks in 2 weeks
    servings_per_day = 0.5 * 6 # Tricia drinks half a container a day, which is 3 servings
    servings_per_two_weeks = servings_per_day * 14

    # Determine the number of containers Tricia needs to buy
    containers_needed = servings_per_two_weeks / 6 # There are 6 servings per container

    # Determine the total cost of the containers
    cost_per_container = 3.00 # The coffee is on sale for $3.00 a bottle
    total_cost = containers_needed * cost_per_container

    # Display the total cost
    result = total_cost
    return result

print(solution())