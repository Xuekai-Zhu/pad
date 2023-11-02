def solution():
    starting_balance = 400  # The PTA starts with $400
    spent_on_supplies = starting_balance / 4  # They spent a fourth of the money on school supplies
    balance_after_supplies = starting_balance - spent_on_supplies  # Determine how much they have left after buying school supplies
    spent_on_food = balance_after_supplies / 2  # They spent half of what was left on food for the faculty
    remaining_balance = balance_after_supplies - spent_on_food  # Determine how much they have left after buying food

    result = remaining_balance
    return result

print(solution())