def solution():
    # Calculate the revenue from matinee tickets
    matinee_revenue = 5 * 32

    # Calculate the revenue from evening tickets
    evening_revenue = 7 * 40

    # Calculate the revenue from opening night tickets
    opening_night_revenue = 10 * 58
    
    # Calculate the total ticket revenue
    ticket_revenue = matinee_revenue + evening_revenue + opening_night_revenue
    
    # Calculate the revenue from popcorn sales
    popcorn_revenue = 10 * ((32 + 40 + 58) / 2)

    # Calculate the total revenue
    total_revenue = ticket_revenue + popcorn_revenue

    result = total_revenue
    return result

print(solution())