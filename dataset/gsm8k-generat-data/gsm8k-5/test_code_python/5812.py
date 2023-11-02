def solution():
    # Calculate the total amount of oil in milliliters
    total_oil_mL = 200 * 20  # Each bottle contains 200 mL, and there are 20 bottles

    # Convert the total amount of oil to liters
    total_oil_L = total_oil_mL / 1000

    result = total_oil_L
    return result

print(solution())