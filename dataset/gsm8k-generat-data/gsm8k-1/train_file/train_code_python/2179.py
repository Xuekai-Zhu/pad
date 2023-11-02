def solution():
    """A group of six friends planned to buy a car. The cost of the car is $1700 and they plan to share the cost equally. They had a car wash to help raise funds, which would be taken out of the total cost. The remaining cost would be split between the six friends. At the car wash, they earn $500. However, Brad decided not to join in the purchase of the car. How much more does each friend have to pay now that Brad isn't participating?"""
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