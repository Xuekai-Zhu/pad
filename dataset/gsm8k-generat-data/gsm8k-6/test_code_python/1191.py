def solution():
    # Calculate the total cost of 101 bears
    first_bear_price = 4.00  # price of the first bear
    discount = 0.50  # discount per bear after the first
    num_bears = 101  # number of bears purchased
    total_cost = first_bear_price + discount*(num_bears-1)  # formula for total cost with discount
    result = total_cost
    return result

print(solution())