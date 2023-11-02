def solution():
    original_win = 45
    mother_gift = 80
    final_balance = 10 + 2 * original_win

    # Calculate the total amount Nigel had after his mother's gift
    total_amount = original_win + mother_gift

    # Calculate the amount Nigel gave away
    amount_given = total_amount - final_balance
    result = amount_given
    return result

print(solution())