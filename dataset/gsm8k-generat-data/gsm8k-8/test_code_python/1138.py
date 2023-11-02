def solution():
    # Define the starting point and increase amount
    savings = 20
    increase_amount = 10

    # Calculate savings for each of the next 4 weeks (a month)
    for i in range(4):
        savings += (savings + increase_amount)

    result = savings
    return result

print(solution())