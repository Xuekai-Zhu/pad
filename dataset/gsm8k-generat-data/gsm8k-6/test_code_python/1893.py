def solution():
    # Calculate the total cost of gas for the trip
    gas_cost = (600 / 20) * 4  # 600 miles / 20 miles per gallon * $4.00/gallon

    # Calculate the total earnings from the trip
    earnings = 0.50 * 600  # $0.50/mile * 600 miles

    # Calculate the profit from the trip
    profit = earnings - gas_cost
    result = profit
    return result

print(solution())