def solution():
    """Tricia buys large bottles of iced coffee that have 6 servings per container. She drinks half a container a day. The coffee is currently on sale for $3.00 a bottle. How much will it cost her to buy enough bottles to last for 2 weeks?"""
    servings_per_bottle = 6
    servings_per_day = 0.5  # Half a container
    days_in_two_weeks = 14
    total_servings_needed = servings_per_day * days_in_two_weeks
    bottles_needed = total_servings_needed / servings_per_bottle
    cost_per_bottle = 3.00
    total_cost = bottles_needed * cost_per_bottle
    result = total_cost
    return result

print(solution())