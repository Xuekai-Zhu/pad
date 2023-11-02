def solution():
    money = 2000  # Emma got $2000 from the bank
    furniture_cost = 400  # Emma bought $400 of furniture
    remaining_money = money - furniture_cost  # Emma has the remaining money after buying furniture
    anna_share = (3/4) * remaining_money  # Emma gave 3/4 of the remaining money to Anna

    # Calculate the money left with Emma
    remaining_money = remaining_money - anna_share
    result = remaining_money
    return result

print(solution())