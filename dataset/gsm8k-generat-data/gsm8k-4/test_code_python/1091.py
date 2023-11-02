def solution():
    """Harper drinks a 1/2 bottle of mineral water per day. She buys the mineral water by the case at a big box store. They come 24 bottles to a case and are currently on sale for $12.00. If she wants to buy enough cases to last her 240 days, how much will she spend?"""
    # Define the number of days Harper wants to last with the water
    days = 240

    # Define the number of bottles Harper drinks per day
    bottles_per_day = 1/2

    # Define the number of bottles per case
    bottles_per_case = 24

    # Calculate the total number of bottles Harper needs
    total_bottles = days * bottles_per_day

    # Calculate the total number of cases Harper needs
    total_cases = total_bottles / bottles_per_case

    # Calculate the total cost of the cases
    total_cost = total_cases * 12

    result = total_cost
    return result

print(solution())