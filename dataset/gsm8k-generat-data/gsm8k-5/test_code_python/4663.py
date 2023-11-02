def solution():
    price_per_liter = 1.4  # Mr. Deane has to pay $1.4 per liter of gas
    friday_price = price_per_liter - 0.4  # The price per liter on Friday will be $0.4 cheaper
    first_purchase = 10  # Mr. Deane fills up 10 liters of gas today
    second_purchase = 25  # Mr. Deane will fill up another 25 liters on Friday

    # Calculate the total cost for the first purchase
    first_cost = first_purchase * price_per_liter

    # Calculate the total cost for the second purchase
    second_cost = second_purchase * friday_price

    # Calculate the total cost for both purchases
    total_cost = first_cost + second_cost
    result = total_cost
    return result

print(solution())