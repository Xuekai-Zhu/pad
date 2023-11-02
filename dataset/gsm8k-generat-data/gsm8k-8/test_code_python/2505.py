def solution():
    necklace_cost = 34
    book_cost = necklace_cost + 5
    total_cost = necklace_cost + book_cost
    limit = 70
    over_limit = total_cost - limit
    result = over_limit
    return result

print(solution())