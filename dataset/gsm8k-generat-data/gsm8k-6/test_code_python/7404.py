def solution():
    # Calculate the total cost of searching for 10 days
    cost = 100 * 5 + 60 * (10 - 5)  # $100 per day for the first 5 days, $60 per day for every day after that
    result = cost
    return result

print(solution())