def solution():
    original_amount = 45  # amount Nigel won
    final_amount = 10 + 2 * original_amount  # final amount Nigel has
    mother_gave = 80  # amount Nigel's mother gave
    total_amount = final_amount - mother_gave  # total amount Nigel had before giving away money
    amount_given_away = original_amount - total_amount  # amount Nigel gave away
    result = amount_given_away
    return result

print(solution())