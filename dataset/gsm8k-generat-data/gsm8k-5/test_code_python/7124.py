def solution():
    orange_price_before = 40  # The price of an orange before the increase
    mango_price_before = 50  # The price of a mango before the increase
    price_increase_percentage = 15  # The percentage increase due to Coronavirus

    # Calculate the new prices after the increase
    orange_price_after = orange_price_before + (orange_price_before * price_increase_percentage / 100)
    mango_price_after = mango_price_before + (mango_price_before * price_increase_percentage / 100)

    # Calculate the total cost of buying ten oranges and ten mangoes at the new prices
    total_cost = (orange_price_after * 10) + (mango_price_after * 10)

    result = total_cost
    return result

print(solution())