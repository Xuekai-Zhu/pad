def solution():
    starting_amount = 9  # Oliver starts with $9
    allowance_saved = 5  # Oliver saves $5 from his allowance
    frisbee_cost = 4  # Oliver spends $4 on a frisbee
    puzzle_cost = 3  # Oliver spends $3 on a puzzle
    birthday_gift = 8  # Oliver's friend gives him $8 as a birthday gift

    # Calculate Oliver's total amount of money
    total_amount = starting_amount + allowance_saved - frisbee_cost - puzzle_cost + birthday_gift

    result = total_amount
    return result

print(solution())