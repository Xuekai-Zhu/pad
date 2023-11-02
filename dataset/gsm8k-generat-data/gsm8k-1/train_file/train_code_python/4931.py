def solution():
    """A movie theater charges $5 for matinee tickets, $7 for evening tickets, and $10 for opening night tickets. A bucket of popcorn costs $10. On Friday, they had 32 matinee customers, 40 evening customers, and 58 customers for an opening night showing of a movie. If half the customers bought popcorn, how much money in dollars did the theater make on Friday night?"""
    matinee_price = 5
    evening_price = 7
    opening_price = 10
    popcorn_price = 10
    matinee_customers = 32
    evening_customers = 40
    opening_customers = 58
    popcorn_customers = (matinee_customers + evening_customers + opening_customers) / 2
    total_matinee_sales = matinee_customers * matinee_price
    total_evening_sales = evening_customers * evening_price
    total_opening_sales = opening_customers * opening_price
    total_popcorn_sales = popcorn_customers * popcorn_price
    total_sales = total_matinee_sales + total_evening_sales + total_opening_sales + total_popcorn_sales
    result = total_sales
    return result

print(solution())