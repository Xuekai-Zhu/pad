def solution():
    # Calculate total revenue from selling the 6 pairs of shoes and 18 shirts
    total_revenue = (6 * 3) + (18 * 2)  # 6 pairs of shoes at $3 each and 18 shirts at $2 each
    # Calculate the amount each of them will earn if they divide their total revenue equally
    amount_each = total_revenue / 2  # dividing the total revenue equally between two people
    result = amount_each
    return result

print(solution())