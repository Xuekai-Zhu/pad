def solution():
    monthly_income = 2000.00  # Jessica makes $2,000.00 a month
    percentage_to_set = 0.25  # Jessica sets 25% of her paycheck aside to put towards fancy shoes
    cost_per_pair = 1000.00  # Each pair of shoes she buys costs $1,000.00
    months_per_year = 12  # There are 12 months in a year

    # Calculate the amount of money Jessica has to set towards fancy shoes
    money_to_set = monthly_income * percentage_to_set

    # Calculate the number of shoes Jessica can buy in a year
    shoes_per_month = money_to_set / money_to_set
    shoes_per_year = shoes_per_month * 12
    result = shoes_per_year
    return result

print(solution())