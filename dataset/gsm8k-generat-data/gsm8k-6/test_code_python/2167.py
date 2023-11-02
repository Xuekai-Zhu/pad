def solution():
    # Calculate the distance the truck driver can drive in 10 hours
    distance = 10 * 30 * 10  # 10 miles per gallon * 30 miles per hour * 10 hours

    # Calculate the amount of gas required for the distance
    gas = distance / 10  # 10 miles per gallon

    # Calculate the cost of the gas
    gas_cost = gas * 2  # $2 per gallon

    # Calculate the amount of money earned for the distance
    money_earned = distance * 0.5  # $.50 per mile

    # Calculate the profit
    profit = money_earned - gas_cost

    result = profit
    return result

print(solution())