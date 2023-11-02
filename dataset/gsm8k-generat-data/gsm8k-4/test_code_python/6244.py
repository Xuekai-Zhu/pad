def solution():
    """Tony decided to rent a small cottage.  The master bedroom and bath totaled 500 sq ft.  The 2 guest bedrooms were 200 sq ft each.  And the kitchen, guest bath and living area totaled 600 sq ft.  If Tony spends $3,000 a month on rent, how much money is he spending per sq ft of house?"""
    # Define the square footage of each area
    master_bed_bath = 500
    guest_bed1 = 200
    guest_bed2 = 200
    kitchen_bath_living = 600

    # Calculate the total square footage
    total_sq_ft = master_bed_bath + guest_bed1 + guest_bed2 + kitchen_bath_living

    # Calculate the cost per square foot
    cost_per_sq_ft = 3000 / total_sq_ft

    # Round the answer to two decimal places
    result = round(cost_per_sq_ft, 2)
    return result

print(solution())