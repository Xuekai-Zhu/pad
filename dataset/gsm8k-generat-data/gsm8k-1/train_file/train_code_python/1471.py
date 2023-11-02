def solution():
    """Shara borrowed money from her brother 6 months ago. She returned $10 per month to her brother. Currently, she was able to return half of the money she borrowed. How much will she still owe her brother 4 months from now?"""
    total_borrowed = 6 * 10
    amount_returned = total_borrowed / 2
    amount_remaining = total_borrowed - amount_returned
    amount_remaining -= 4 * 10
    result = amount_remaining
    return result

print(solution())