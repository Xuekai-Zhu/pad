def solution():
    
    total_cost = 1700
    car_wash_funds = 500
    remaining_cost = total_cost - car_wash_funds
    num_friends = 6
    cost_per_friend = remaining_cost / num_friends
    cost_per_friend_without_brad = remaining_cost / (num_friends - 1)
    additional_cost_per_friend = cost_per_friend_without_brad - cost_per_friend
    result = additional_cost_per_friend
    return result

print(solution())