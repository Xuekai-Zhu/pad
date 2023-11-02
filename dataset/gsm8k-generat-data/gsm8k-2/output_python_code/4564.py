def solution():
    """Yoque borrowed money from her sister. She promised to pay it back in 11 months including an additional 10% of the money she borrowed. If she pays $15 per month, how much money did she borrow?"""
    total_paid = 15 * 11
    final_amount = total_paid / 1.1
    borrowed_amount = final_amount - total_paid
    result = borrowed_amount
    return result

print(solution())