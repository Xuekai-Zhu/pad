def solution():
    matinee_tickets = 32
    evening_tickets = 40
    opening_night_tickets = 58
    popcorn_customers = (matinee_tickets + evening_tickets + opening_night_tickets) / 2
    popcorn_cost = 10
    matinee_price = 5
    evening_price = 7
    opening_night_price = 10

    # Calculate the total revenue from matinee tickets
    total_matinee_revenue = matinee_tickets * matinee_price

    # Calculate the total revenue from evening tickets
    total_evening_revenue = evening_tickets * evening_price

    # Calculate the total revenue from opening night tickets
    total_opening_night_revenue = opening_night_tickets * opening_night_price

    # Calculate the total revenue from popcorn
    total_popcorn_revenue = popcorn_customers * popcorn_cost

    # Calculate the total revenue from all sources
    total_revenue = total_matinee_revenue + total_evening_revenue + total_opening_night_revenue + total_popcorn_revenue
    result = total_revenue
    return result

print(solution())