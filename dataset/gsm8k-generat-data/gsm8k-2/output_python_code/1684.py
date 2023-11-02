def solution():
    """Clinton buys a burger meal for lunch for $6.00 and up sizes his fries and drinks for $1.00 more. If Clinton buys this same meal every day for 5 days, how much does he spend on lunch?"""
    burger_price = 6
    upsized_price = 7
    num_days = 5
    total_spent = (burger_price + upsized_price * 2) * num_days
    result = total_spent
    return result

print(solution())