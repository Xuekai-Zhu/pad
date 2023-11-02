def solution():
    rene_money = 300
    florence_money = (1/2) * (1/3) * maria_money
    rene_factor = 3
    isha_money = (1/3) * maria_money - florence_money - rene_money
    total_money_given = isha_money + florence_money + rene_money
    result = total_money_given
    return result

# Note: This solution assumes that the total amount of money Maria had is not given in the question. Therefore, we cannot find the exact amount of money that she gave to her friends. We can only find the total amount given to all three friends.

print(solution())