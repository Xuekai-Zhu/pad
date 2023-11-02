def solution():
    """Howard spends $8 dollars at the arcade on Monday. On Tuesday, he spends twice as much at the arcade as he did on Monday. On Wednesday, he spends 4 times as much at the arcade as he spent on Tuesday. If he originally had $100, how much money does he have left?"""
    monday_spending = 8
    tuesday_spending = 2 * monday_spending
    wednesday_spending = 4 * tuesday_spending
    total_spending = monday_spending + tuesday_spending + wednesday_spending
    original_amount = 100
    amount_left = original_amount - total_spending
    result = amount_left
    return result

print(solution())