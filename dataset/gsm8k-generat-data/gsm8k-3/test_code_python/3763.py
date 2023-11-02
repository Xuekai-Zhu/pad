def solution():
    """Cooper makes 7 apple pies a day. He does this for 12 days. Ashley then eats 50 of his pies. How many apple pies remain with Cooper?"""
    # Define the number of pies Cooper makes each day and the number of days he makes them
    pies_per_day = 7
    days = 12

    # Calculate the total number of pies Cooper makes
    total_pies = pies_per_day * days

    # Calculate the number of pies left after Ashley eats 50
    pies_left = total_pies - 50

    # Display the number of pies remaining with Cooper
    result = pies_left
    return result

print(solution())