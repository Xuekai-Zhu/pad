def solution():
    house_price = 400000  # Mr. Tan sold his house for $400000
    transfer_fee = 0.75 * house_price  # Mr. Tan paid the transfer fees that amount to 3% of the selling price
    brokerage_fee = 0.05 * house_price  # Mr. Tan paid a brokerage fee that is 5% of the selling price
    remaining_price = house_price - transfer_fee - brokerage_fee  # Mr. Tan's remaining loan amount

    # Calculate the net profit from selling the house
    net_proceeds = house_price - transfer_fee - remaining_price
    result = net_proceeds
    return result

print(solution())