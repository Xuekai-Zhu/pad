def solution():
    # Calculate the revenue from matinee tickets
    matinee_revenue = 5 * 32  # $5 per ticket, 32 customers

    # Calculate the revenue from evening tickets
    evening_revenue = 7 * 40  # $7 per ticket, 40 customers

    # Calculate the revenue from opening night tickets
    opening_night_revenue = 10 * 58  # $10 per ticket, 58 customers

    # Calculate the revenue from popcorn sales
    popcorn_revenue = 10 * (32 + 40 + 58) / 2  # $10 per bucket, sold to half the customers

    # Calculate the total revenue for the theater on Friday night
    total_revenue = matinee_revenue + evening_revenue + opening_night_revenue + popcorn_revenue
    result = total_revenue
    return result

print(solution())