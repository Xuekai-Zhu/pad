def solution():
    # Calculate the total amount James spent
    total_spent = 3000

    # Calculate the amount James gets back from returning the TV and bike
    return_amount = 700 + 500

    # Calculate the cost of the bike James sold
    sold_bike_cost = 500 * 1.2

    # Calculate the amount James got for selling the bike
    sold_bike_amount = sold_bike_cost * 0.8

    # Calculate the total cost of the items after returns and sales
    total_cost = total_spent - return_amount + sold_bike_cost - sold_bike_amount + 100

    result = total_cost
    return result

print(solution())