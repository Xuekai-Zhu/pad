def solution():
    num_boys = 40
    boy_price = 50
    girl_price = boy_price / 2
    num_girls = num_boys / 4

    # Calculate the total amount of money collected from boys
    total_boys_money = num_boys * boy_price

    # Calculate the total amount of money collected from girls
    total_girls_money = num_girls * girl_price

    # Calculate the total amount of money collected at the party
    total_money_collected = total_boys_money + total_girls_money
    result = total_money_collected
    return result

print(solution())