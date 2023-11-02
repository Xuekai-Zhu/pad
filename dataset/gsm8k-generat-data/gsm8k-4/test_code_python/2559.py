def solution():
    """Ben's new car cost twice as much as his old car. He sold his old car for $1800 and used that to pay off some of the cost of his new car. He still owes another $2000 on his new car. How much did his old car cost, in dollars?"""

    # Calculate the total cost of the new car
    new_car_cost = 1800 + 2000 + 1800*2
    
    # Calculate the cost of the old car
    old_car_cost = (new_car_cost - 1800)//2

    # Return the cost of the old car
    result = old_car_cost
    return result

print(solution())