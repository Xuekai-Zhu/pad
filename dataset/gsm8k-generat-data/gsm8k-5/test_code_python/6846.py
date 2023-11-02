def solution():
    giselle_money = 120  # Giselle has $120
    isabella_money = giselle_money + 15  # Isabella has $15 more than Giselle
    sam_money = isabella_money - 45  # Sam has $45 less than Isabella

    # Calculate the total amount of money
    total_money = giselle_money + isabella_money + sam_money

    # Calculate the amount of money each shopper will receive if they share it equally
    amount_each = total_money / 3
    result = amount_each
    return result

print(solution())