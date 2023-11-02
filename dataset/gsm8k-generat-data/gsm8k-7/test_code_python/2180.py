def solution():
    num_friends = 6
    car_cost = 1700
    carwash_funds = 500
    brad_share = car_cost / num_friends
    total_cost = car_cost - carwash_funds
    remaining_friends = num_friends - 1
    remaining_cost = total_cost - brad_share
    cost_per_friend = remaining_cost / remaining_friends
    difference = brad_share - cost_per_friend
    result = difference
    return result

print(solution())