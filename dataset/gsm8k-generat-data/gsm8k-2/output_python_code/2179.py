def solution():
    """A group of six friends planned to buy a car. The cost of the car is $1700 and they plan to share the cost equally. They had a car wash to help raise funds, which would be taken out of the total cost. The remaining cost would be split between the six friends. At the car wash, they earn $500. However, Brad decided not to join in the purchase of the car. How much more does each friend have to pay now that Brad isn't participating?"""
    car_cost = 1700
    num_friends = 6
    brad_share = car_cost / num_friends
    total_raised = 500
    car_cost -= total_raised
    num_friends -= 1
    new_share = car_cost / num_friends
    difference = new_share - brad_share
    result = difference
    return result

print(solution())