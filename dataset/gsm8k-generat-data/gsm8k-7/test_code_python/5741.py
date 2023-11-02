def solution():
    hair_cost = 50
    manicure_cost = 30
    tip_percent = 0.20

    # Calculate the tip for the hair stylist
    hair_tip = hair_cost * tip_percent

    # Calculate the total cost for the hair stylist, including tip
    hair_total = hair_cost + hair_tip

    # Calculate the tip for the manicurist
    manicure_tip = manicure_cost * tip_percent

    # Calculate the total cost for the manicurist, including tip
    manicure_total = manicure_cost + manicure_tip

    # Calculate the total cost for both services
    total_cost = hair_total + manicure_total
    result = total_cost
    return result

print(solution())