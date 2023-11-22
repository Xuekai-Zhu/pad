def solution():
    
    budget = 90
    tokens_per_round = 5
    rides_per_round = 2
    cost_per_ride = 10
    total_tokens = tokens_per_round * 2
    total_cost = total_tokens * cost_per_round
    num_friends = budget / total_cost
    result = num_friends
    return result

print(solution())