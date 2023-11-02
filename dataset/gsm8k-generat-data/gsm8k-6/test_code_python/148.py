def solution():
    lottery_won = 50  # amount won in the lottery
    tax = 0.2 * lottery_won  # tax to be paid
    processing_fee = 5  # processing fee to be paid
    take_home_amount = lottery_won - tax - processing_fee  # amount Winwin was able to take home
    result = take_home_amount
    return result

print(solution())