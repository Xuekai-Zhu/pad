def solution():
    current_speed = 10  # current internet speed in Mbps
    current_bill = 20  # current monthly bill in dollars
    price_30Mbps = 2 * current_bill  # price of 30 Mbps in dollars per month
    price_20Mbps = current_bill + 10  # price of 20 Mbps in dollars per month
    difference = price_30Mbps - price_20Mbps  # difference in cost between 30 Mbps and 20 Mbps
    savings_per_month = difference  # savings per month if Marites chooses 20 Mbps
    savings_per_year = savings_per_month * 12  # savings per year if Marites chooses 20 Mbps
    result = savings_per_year
    return result

print(solution())