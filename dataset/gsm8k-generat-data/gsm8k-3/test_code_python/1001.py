def solution():
    """A plant supplier was able to sell 20 pieces of orchids for $50 each and 15 pieces potted Chinese money plant for $25. The money he earned was then used to pay his two workers $40 each and to buy new pots worth $150. How much money was left from the plant supplier's earnings?"""
    # Calculate the earnings from selling orchids
    orchid_earnings = 20 * 50

    # Calculate the earnings from selling Chinese money plant
    chinese_money_earnings = 15 * 25

    # Calculate the total earnings
    total_earnings = orchid_earnings + chinese_money_earnings

    # Calculate the total expenses
    worker_expenses = 2 * 40
    pot_expenses = 150
    total_expenses = worker_expenses + pot_expenses

    # Calculate the money left from the earnings
    money_left = total_earnings - total_expenses

    # Display the money left
    result = money_left
    return result

print(solution())