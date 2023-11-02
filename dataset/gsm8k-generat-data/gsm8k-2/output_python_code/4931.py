def solution():
    """A movie theater charges $5 for matinee tickets, $7 for evening tickets, and $10 for opening night tickets. A bucket of popcorn costs $10. On Friday, they had 32 matinee customers, 40 evening customers, and 58 customers for an opening night showing of a movie. If half the customers bought popcorn, how much money in dollars did the theater make on Friday night?"""
    matinee_price = 5
    evening_price = 7
    opening_night_price = 10
    popcorn_price = 10
    matinee_customers = 32
    evening_customers = 40
    opening_night_customers = 58
    total_customers = matinee_customers + evening_customers + opening_night_customers
    half_popcorn_customers = total_customers / 2
    total_sales = (matinee_customers * matinee_price) + (evening_customers * evening_price) + (opening_night_customers * opening_night_price) + (half_popcorn_customers * popcorn_price)
    result = total_sales
    return result

print(solution())