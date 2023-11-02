def solution():
    """Harper drinks a 1/2 bottle of mineral water per day.  She buys the mineral water by the case at a big box store.  They come 24 bottles to a case and are currently on sale for $12.00.  If she wants to buy enough cases to last her 240 days, how much will she spend?"""
    # Calculate the number of bottles Harper will need for 240 days
    num_bottles = 240 * 0.5

    # Calculate the number of cases Harper will need (rounded up to the nearest whole case)
    num_cases = (num_bottles / 24)

    # Calculate the total cost of the cases of mineral water
    total_cost = num_cases * 12

    # Display the total cost
    result = total_cost
    return result

print(solution())