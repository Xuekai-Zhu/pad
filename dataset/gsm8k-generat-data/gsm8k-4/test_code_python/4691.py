def solution():
    """Jerry was contracted to work on a house by his neighbor Miss Stevie. The time it took him to fix the broken kitchen counter was three times longer than the time he took painting the house. He took 8 hours painting the house and then helped mow Miss Stevie's lawn, taking 6 hours. If he charged Miss Stevie $15 per hour of work, calculate the amount of money that Miss Stevie paid him."""
    # Calculate the time it took Jerry to fix the kitchen counter
    kitchen_time = 3 * 8

    # Calculate the total time Jerry spent on the house
    total_time = 8 + kitchen_time + 6

    # Calculate the total amount of money Miss Stevie paid Jerry
    total_payment = total_time * 15

    result = total_payment
    return result

print(solution())