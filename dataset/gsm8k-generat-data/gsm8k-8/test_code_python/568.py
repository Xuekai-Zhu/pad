def solution():
    # Calculate the total cost of raising the child from birth to age 18
    total_cost = 0
    for i in range(1, 9):
        total_cost += 10000
    for i in range(9, 19):
        total_cost += 20000
    total_cost += 250000

    # Calculate John's half of the total cost
    john_cost = total_cost / 2
    result = john_cost
    return result

print(solution())