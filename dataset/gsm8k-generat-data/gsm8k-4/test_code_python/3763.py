def solution():
    """Cooper makes 7 apple pies a day. He does this for 12 days. Ashley then eats 50 of his pies. How many apple pies remain with Cooper?"""
    # Define the number of apple pies made each day and the number of days
    pies_per_day = 7
    days = 12

    # Calculate the total number of apple pies made
    total_pies = pies_per_day * days

    # Subtract the number of pies eaten by Ashley
    pies_remaining = total_pies - 50

    # return the result
    result = pies_remaining
    return result

print(solution())