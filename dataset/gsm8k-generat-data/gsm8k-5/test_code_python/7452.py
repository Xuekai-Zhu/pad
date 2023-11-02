def solution():
    bonus = 900  # Gwen received a $900 bonus
    amount_per_stock = bonus / 3  # Gwen spent one-third of her bonus on each stock

    # Calculate the value of stock A after one year
    value_A = 2 * amount_per_stock

    # Calculate the value of stock B after one year
    value_B = 2 * amount_per_stock

    # Calculate the value of stock C after one year
    value_C = 0.5 * amount_per_stock

    # Calculate the total value of all stocks after one year
    total_value = value_A + value_B + value_C
    result = total_value
    return result

print(solution())