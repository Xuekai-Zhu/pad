def solution():
    num_friends = 8
    friend_gift_cost = 9
    total_friend_gift_cost = num_friends * friend_gift_cost

    # Calculate the total cost of all gifts excluding the friends' gifts
    total_gift_cost_ex_friends = total_gift_cost - total_friend_gift_cost

    # Calculate the cost per gift for Jaco's mother and father
    cost_per_gift_mom_dad = total_gift_cost_ex_friends / 2

    result = cost_per_gift_mom_dad
    return result

print(solution())