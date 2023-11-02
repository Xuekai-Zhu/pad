def solution():
    initial_money = 150  # Inez starts with $150
    remaining_money = 25  # Inez has $25 remaining after buying skates

    # Calculate how much Inez spent on skates
    skates_cost = initial_money / 2

    # Calculate how much Inez spent on pads
    pads_cost = initial_money - skates_cost - remaining_money

    # Calculate the total cost of the pads
    total_pads_cost = pads_cost * 2
    result = total_pads_cost
    return result

print(solution())