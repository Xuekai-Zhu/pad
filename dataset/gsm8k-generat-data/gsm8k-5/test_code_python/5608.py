def solution():
    # Calculate the total revenue from selling watermelons
    total_revenue = 105 + (18 * 3)  # $105 profit plus sales from 18 watermelons at $3 each

    # Determine how many watermelons Carl started with
    # We can use trial and error starting from 1 until we reach the total revenue
    watermelons = 1
    while watermelons * 3 < total_revenue:
        watermelons += 1

    result = watermelons
    return result

print(solution())