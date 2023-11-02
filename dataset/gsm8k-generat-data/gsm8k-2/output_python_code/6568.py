def solution():
    """Ali and Leila reserve their places for a trip to Egypt. The price is $147 per person, but they were each given a discount of $14 since there are two of them. How much does their trip cost?"""
    price_per_person = 147
    discount_per_person = 14
    total_discount = discount_per_person * 2
    total_price = price_per_person * 2 - total_discount
    result = total_price
    return result

print(solution())