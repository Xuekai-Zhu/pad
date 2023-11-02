def solution():
    initial_cost = 200  # cost of the games when Tom bought them
    final_value = initial_cost * 3  # value of the games after they tripled in value
    sold_percent = 0.4  # percentage of games sold
    sold_value = sold_percent * final_value  # value of the games sold
    result = sold_value
    return result

print(solution())