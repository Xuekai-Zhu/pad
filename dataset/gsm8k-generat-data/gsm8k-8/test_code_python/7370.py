def solution():
    # Define number of free and paid lessons
    free_lessons = 1
    paid_lessons = 10 + ((20-1) - 10) // 2   # only needs to pay for every other lesson after the first 10

    # Calculate total cost
    total_cost = (free_lessons * 0) + (paid_lessons * 5)

    # Calculate James' portion of cost (after uncle pays half)
    james_cost = total_cost / 2

    return james_cost

print(solution())