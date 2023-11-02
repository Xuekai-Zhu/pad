def solution():
    guests = 15  # Carl is inviting 15 guests
    glasses_per_person = 2  # Carl wants each person to have at least 2 glasses of punch
    ounces_per_glass = 12  # Each glass holds 12 ounces of punch

    # Calculate the total ounces of punch needed
    total_ounces = guests * glasses_per_person * ounces_per_glass
    result = total_ounces
    return result

print(solution())