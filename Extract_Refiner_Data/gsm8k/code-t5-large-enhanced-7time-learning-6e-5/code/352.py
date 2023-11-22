def solution():
    
    # Define the initial amount of money Dean has
    initial_money = 28

    # Define the cost of each item
    toy_car_cost = 2
    teddy_bear_cost = 1

    # Define the number of toy cars and teddy bears purchased
    num_toy_cars = 6
    num_teddy_bears = 5

    # Calculate the total cost of the purchased items
    total_cost = (toy_car_cost * num_toy_cars) + (teddy_bear_cost * num_teddy_bears)

    # Add the extra money Dean's mother gave him
    total_cost += 10

    # Calculate the remaining money Dean has
    remaining_money = initial_money - total_cost

    # return the result
    result = remaining_money
    return result

print(solution())