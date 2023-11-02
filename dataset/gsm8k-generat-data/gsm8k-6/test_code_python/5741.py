def solution():
    hair_updo_cost = 50
    manicure_cost = 30
    tip_percentage = 0.20

    # Calculate the total cost of the hair updo and manicure services including tips
    hair_updo_tip = hair_updo_cost * tip_percentage
    manicure_tip = manicure_cost * tip_percentage
    total_cost = (hair_updo_cost + hair_updo_tip) + (manicure_cost + manicure_tip)

    result = total_cost
    return result

print(solution())