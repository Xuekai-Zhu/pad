def solution():
    # Solve for Beth's current amount of money
    beth_total = 105 - 35  # If Beth had $35 more, she would have $105

    # Solve for Jan's current amount of money
    jan_total = beth_total + 10  # If Jan had $10 less, he would have the same money as Beth has

    # Calculate the total amount of money they have together
    total_money = beth_total + jan_total
    result = total_money
    return result

print(solution())