def solution():
    # Define the initial amount of money
    initial_money = 158

    # Calculate the cost of the shoes and the bag
    shoe_cost = 45
    bag_cost = shoe_cost - 17

    # Calculate the cost of lunch
    lunch_cost = bag_cost / 4

    # Calculate the total cost of the purchases
    total_cost = shoe_cost + bag_cost + lunch_cost

    # Calculate the amount of money left
    money_left = initial_money - total_cost
    result = money_left
    return result

print(solution())