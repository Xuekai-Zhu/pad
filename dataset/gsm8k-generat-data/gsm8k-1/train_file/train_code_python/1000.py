def solution():
    """
    A plant supplier was able to sell 20 pieces of orchids for $50 each and 15 pieces potted Chinese money plant for $25.
    The money he earned was then used to pay his two workers $40 each and to buy new pots worth $150. How much money was
    left from the plant supplier's earnings?
    """
    orchids_sold = 20
    orchid_price = 50
    chinese_money_plants_sold = 15
    chinese_money_plant_price = 25
    total_orchid_sale = orchids_sold * orchid_price
    total_chinese_money_plant_sale = chinese_money_plants_sold * chinese_money_plant_price
    total_sale = total_orchid_sale + total_chinese_money_plant_sale
    worker_pay = 40 * 2
    pot_cost = 150
    expenses = worker_pay + pot_cost
    money_left = total_sale - expenses
    result = money_left
    return result

print(solution())