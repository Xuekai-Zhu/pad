def solution():
    """Carrie was given ten twenties and 140 quarters by her aunt to use for lunch. If she spent all the quarters and 3/5 of the twenties, calculate the total amount of money she paid for the lunch."""
    num_twenties = 10
    num_quarters = 140
    spent_twenties = num_twenties * (3/5)
    total_spent = (spent_twenties * 20) + (num_quarters * 0.25)
    result = total_spent
    return result

print(solution())