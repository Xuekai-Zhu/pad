def solution():
    """A group of six friends planned to buy a car. The cost of the car is $1700 and they plan to share the cost equally. They had a car wash to help raise funds, which would be taken out of the total cost. The remaining cost would be split between the six friends. At the car wash, they earn $500. However, Brad decided not to join in the purchase of the car. How much more does each friend have to pay now that Brad isn't participating?"""
    # Define the cost of the car and the number of friends
    car_cost = 1700
    num_friends = 6

    # Calculate the cost per friend before the car wash
    cost_per_friend_before = car_cost / num_friends

    # Calculate the total amount raised at the car wash
    carwash_amount = 500

    # Subtract the car wash amount from the car cost
    car_cost -= carwash_amount

    # Calculate the cost per friend after the car wash
    cost_per_friend_after = car_cost / (num_friends - 1)

    # Calculate the difference in cost per friend
    cost_difference = cost_per_friend_after - cost_per_friend_before

    result = round(cost_difference, 2)
    return result

print(solution())