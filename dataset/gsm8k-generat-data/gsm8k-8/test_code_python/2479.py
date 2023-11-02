def solution():
    # Define the prices and the number of packets of chips John wants to buy
    chips_price = 2
    corn_chips_price = 1.5
    num_chips = 15
    total_money = 45

    # Calculate the total cost of the chips John wants to buy
    chips_cost = chips_price * num_chips

    # Calculate the remaining money John has after buying the chips
    remaining_money = total_money - chips_cost

    # Calculate the maximum number of packets of corn chips John can buy
    num_corn_chips = remaining_money / corn_chips_price

    # Round down the number of corn chips to the nearest integer
    num_corn_chips = int(num_corn_chips)

    result = num_corn_chips
    return result

print(solution())