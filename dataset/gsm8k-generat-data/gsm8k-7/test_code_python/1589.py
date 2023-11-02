def solution():
    matinee_tickets = 200
    matinee_price = 5
    evening_tickets = 300
    evening_price = 12
    d3_tickets = 100
    d3_price = 20

    # Calculate the total revenue from matinee tickets
    matinee_revenue = matinee_tickets * matinee_price

    # Calculate the total revenue from evening tickets
    evening_revenue = evening_tickets * evening_price

    # Calculate the total revenue from 3D tickets
    d3_revenue = d3_tickets * d3_price

    # Calculate the total revenue from all ticket sales
    total_revenue = matinee_revenue + evening_revenue + d3_revenue
    result = total_revenue
    return result

print(solution())