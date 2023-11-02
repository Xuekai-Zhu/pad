def solution():
    """Mr. Tan sold his house for $400 000. He paid the transfer fees that amount to 3% of the selling price and also paid a brokerage fee that is 5% of the selling price. If he also paid $250 000 for the remaining loan amount of the house, how much is Mr. Tan's net proceeds from selling the house?"""
    selling_price = 400000
    transfer_fee = selling_price * 0.03
    brokerage_fee = selling_price * 0.05
    remaining_loan = 250000
    net_proceeds = selling_price - transfer_fee - brokerage_fee - remaining_loan
    result = net_proceeds
    return result

print(solution())