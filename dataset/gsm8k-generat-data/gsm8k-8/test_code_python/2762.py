def solution():
    # Calculate the total cost of the kombucha per bottle
    cost_per_bottle = 3.00 - 0.10

    # Calculate the total number of bottles consumed in a year
    total_bottles = 15 * 12

    # Calculate the total cost of all the bottles consumed in a year
    total_cost = cost_per_bottle * total_bottles

    # Calculate the total cash refund from recycling all the bottles consumed in a year
    cash_refund = total_bottles * 0.10

    # Calculate the total number of bottles of kombucha Henry can buy with the cash refund
    bottles_bought = cash_refund / cost_per_bottle
    result = bottles_bought
    return result

print(solution())