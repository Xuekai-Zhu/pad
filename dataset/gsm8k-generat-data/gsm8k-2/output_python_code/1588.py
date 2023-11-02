def solution():
    """The movie theater sells matinee tickets for $5, evening tickets for $12, and 3D tickets for $20. If they sell 200 matinee tickets, 300 evening tickets and 100 3D tickets, how much money do they make in total?"""
    matinee_tickets = 200
    evening_tickets = 300
    three_d_tickets = 100
    matinee_price = 5
    evening_price = 12
    three_d_price = 20
    total_sales = (matinee_tickets * matinee_price) + (evening_tickets * evening_price) + (three_d_tickets * three_d_price)
    result = total_sales
    return result

print(solution())