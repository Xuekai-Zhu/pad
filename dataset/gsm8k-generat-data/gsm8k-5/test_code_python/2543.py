def solution():
    glasses_per_day = 4  # Matthew drinks 4 glasses of water per day
    ounces_per_glass = 5  # Each glass is 5 ounces
    ounces_per_week = glasses_per_day * 7 * ounces_per_glass  # Calculate total ounces per week
    bottles_per_week = ounces_per_week // 35  # Calculate number of times a 35-ounce bottle will be filled
    result = bottles_per_week
    return result

print(solution())