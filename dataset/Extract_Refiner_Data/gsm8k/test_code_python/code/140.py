def solution():
    
    # Define the number of clients and the required prices
    num_clients = 8
    bleach_price = 2
    cloths_price = 5

    # Calculate the total cost of bleach and cloths for one client
    total_cost = (2 * bleach_price) + (cloths_price * 5)

    # Calculate the total income for one client
    total_income = num_clients * total_cost

    # Calculate the profit for one client
    profit = 92 - total_income

    # return the result
    result = profit
    return result

print(solution())