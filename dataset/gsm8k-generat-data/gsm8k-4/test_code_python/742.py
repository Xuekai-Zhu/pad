def solution():
    """Brendan can cut 8 yards of grass per day, he bought a lawnmower and it helped him to cut more yards by Fifty percent per day. How many yards will Brendan be able to cut after a week?"""
    # Define Brendan's initial cutting capacity
    initial_capacity = 8

    # Define the increase in capacity due to the lawnmower
    lawnmower_increase = 0.5

    # Calculate Brendan's new cutting capacity with the lawnmower
    new_capacity = initial_capacity * (1 + lawnmower_increase)

    # Calculate Brendan's weekly cutting capacity with the lawnmower
    weekly_capacity = new_capacity * 7

    result = weekly_capacity
    return result

print(solution())