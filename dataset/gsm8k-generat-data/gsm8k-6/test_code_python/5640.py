def solution():
    # Calculate the total cost of the printer inks
    total_cost = 2 * 11 + 3 * 15 + 2 * 13  # cost of two black inks, three red inks, and two yellow inks

    # Calculate the remaining amount of money Phantom needs to buy all the printer inks
    remaining_money = total_cost - 50

    result = remaining_money
    return result

print(solution())