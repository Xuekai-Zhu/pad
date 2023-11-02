def solution():
    total_money = 4 * 40  # Leila spent 1/4 of her money on a sweater, so 4/4 * 40 = $160 is her total money
    money_spent_on_sweater = 40  # Leila spent $40 on a sweater
    money_left_for_jewelry = total_money - money_spent_on_sweater - 20  # Leila spent $20 on jewelry after buying the sweater
    money_spent_on_jewelry = total_money - money_spent_on_sweater - money_left_for_jewelry  # Calculate how much Leila spent on jewelry

    # Calculate how much more Leila spent on jewelry than on the sweater
    difference = money_spent_on_jewelry - money_spent_on_sweater
    result = difference
    return result

print(solution())