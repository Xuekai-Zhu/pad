def solution():
    """A plant supplier was able to sell 20 pieces of orchids for $50 each and 15 pieces potted Chinese money plant for $25. The money he earned was then used to pay his two workers $40 each and to buy new pots worth $150. How much money was left from the plant supplier's earnings?"""
    orchid_price = 50
    orchid_quantity = 20
    money_plant_price = 25
    money_plant_quantity = 15
    worker_pay = 40 * 2
    pot_cost = 150
    total_earnings = (orchid_price * orchid_quantity) + (money_plant_price * money_plant_quantity)
    total_expenses = worker_pay + pot_cost
    earnings_left = total_earnings - total_expenses
    result = earnings_left
    return result

print(solution())