def solution():
    borrowed_money = 6 * 10  # Shara borrowed money 6 months ago and returned $10 per month
    returned_money = borrowed_money / 2  # Shara has returned half of the money she borrowed
    remaining_money = borrowed_money - returned_money  # Shara still owes her brother this much money

    # Calculate the remaining amount Shara will owe her brother 4 months from now
    remaining_months = 4
    remaining_payment = remaining_months * 10
    total_remaining = remaining_money - remaining_payment
    result = total_remaining
    return result

print(solution())