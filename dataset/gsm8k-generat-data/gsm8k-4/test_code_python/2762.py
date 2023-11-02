def solution():
    """Henry drinks 15 bottles of kombucha every month. Each bottle costs $3.00 and is eligible for a cash refund of $0.10 per bottle when he takes it to a recycling center. After 1 year, how many bottles of kombucha will he be able to buy after he receives his cash refund?"""
    # Define the number of bottles Henry drinks each month and the cost per bottle
    bottles_per_month = 15
    cost_per_bottle = 3.00

    # Calculate the cost of one year's worth of kombucha
    total_cost = bottles_per_month * 12 * cost_per_bottle

    # Calculate the total cash refund Henry will receive
    total_refund = bottles_per_month * 12 * 0.1

    # Calculate the number of bottles Henry can buy with the cash refund
    bottles_with_refund = total_refund / cost_per_bottle

    # Calculate the total number of bottles Henry can buy in one year including the cash refund
    total_bottles = bottles_per_month * 12 + bottles_with_refund

    result = int(total_bottles)
    return result

print(solution())