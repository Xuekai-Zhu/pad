def solution():
    grapes_per_6_months = 90  # Borris uses 90 kilograms of grapes every 6 months
    increase_percentage = 20  # Borris wants to increase his production by 20%
    total_grapes = grapes_per_6_months * 2  # Borris needs to calculate the grapes he needs in a year, which is 2 times the grapes he uses in 6 months

    # Calculate the new amount of grapes with the 20% increase in production
    new_grapes = total_grapes * (1 + (increase_percentage / 100))

    result = new_grapes
    return result

print(solution())