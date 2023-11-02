def solution():
    total_cost = 1700
    num_friends = 6
    carwash_funds = 500

    cost_per_friend = (total_cost - carwash_funds) / num_friends

    new_num_friends = num_friends - 1
    new_cost_per_friend = total_cost / new_num_friends

    difference_in_cost = new_cost_per_friend - cost_per_friend
    result = difference_in_cost
    return result

print(solution())