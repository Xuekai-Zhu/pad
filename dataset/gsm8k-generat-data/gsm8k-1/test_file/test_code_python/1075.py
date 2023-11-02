def solution():
    """A $2000 watch was put on sale so that Mr. Rogers bought it at 75% of its original price. He then sold the watch to his friend at 120% of the price that he bought it. What is the percentage discount obtained by Mr. Roger's friend from the original price?"""
    original_price = 2000
    purchase_price = original_price * 0.75
    selling_price = purchase_price * 1.2
    discount_percent = (1 - (selling_price / original_price)) * 100
    result = discount_percent
    return result

print(solution())