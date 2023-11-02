def solution():
    # Calculate the total cost for the oranges
    oranges_cost = 1.5 * 4  # Each passenger gets an orange, so the total cost for 4 passengers is 1.5 * 4

    # Calculate the amount saved by not buying oranges at the stop
    amount_saved = oranges_cost

    # Calculate the percentage saved
    total_planned_spending = 15  # The family had planned to spend $15 in total
    percentage_saved = (amount_saved / total_planned_spending) * 100

    result = percentage_saved
    return result

print(solution())