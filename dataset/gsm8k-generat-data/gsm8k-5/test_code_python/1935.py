def solution():
    remaining_amount = 2900  # Reese has $2900 remaining after her expenses in February, March, and April

    # Calculate the total amount spent in February and March
    spent_feb_march = (20 + 40) / 100 * remaining_amount

    # Calculate the initial amount in her savings account
    initial_amount = remaining_amount + spent_feb_march + 1500
    result = initial_amount
    return result

print(solution())