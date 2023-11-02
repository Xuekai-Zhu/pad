def solution():
    # Calculate the amount of money Emma gave to her friend Anna
    remaining_money = 2000 - 400  # Emma spent $400 on furniture
    anna_money = (3/4) * remaining_money

    # Calculate the amount of money left with Emma
    emma_money = remaining_money - anna_money
    result = emma_money
    return result

print(solution())