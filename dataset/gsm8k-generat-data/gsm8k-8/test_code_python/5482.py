def solution():
    # Calculate total ounces of water Rachel drinks
    total_ounces = 2 * 10 + 4 * 10 + 3 * 10 * 4
    # Subtract the total from Sunday to Friday to find how much Rachel needs to drink on Saturday
    ounces_remaining = 220 - total_ounces
    # Convert remaining ounces to number of glasses of water
    glasses_on_saturday = ounces_remaining/10
    result = glasses_on_saturday
    return result

print(solution())