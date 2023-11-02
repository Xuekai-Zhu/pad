def solution():
    # Calculate the total cost of the lessons
    cost_of_10_lessons = 10 * 5  # first 10 lessons
    cost_of_10_alternate_lessons = ((20-1-10)//2 + 1) * 5  # alternate lessons
    total_cost = cost_of_10_lessons + cost_of_10_alternate_lessons  # total cost of the lessons
    James_pays = total_cost / 2  # James' uncle pays for half of the cost
    result = James_pays
    return result

print(solution())