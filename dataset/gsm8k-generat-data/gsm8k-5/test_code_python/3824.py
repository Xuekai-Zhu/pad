def solution():
    rene_money = 300  # Maria's cousin Rene received $300
    florence_money = 3 * rene_money / 2  # Florence received half of what Maria gave to Isha and three times as much as Rene
    isha_money = florence_money / 2  # Isha received a third of Maria's money

    # Calculate the total amount of money Maria gave to her three friends
    total_money = isha_money + florence_money + rene_money
    result = total_money
    return result

print(solution())