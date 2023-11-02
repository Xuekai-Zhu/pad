def solution():
    num_parents = 2
    num_brothers = 3
    num_nephews = num_brothers * 2  # Each brother has 2 children

    total_gifts = num_parents + num_brothers + num_nephews
    cost_per_gift = 5

    total_cost = total_gifts * cost_per_gift
    result = total_cost
    return result

print(solution())