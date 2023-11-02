def solution():
    # Calculate Nancy's weight based on her daily water intake
    water_intake_percentage = 0.6  # Nancy drinks 60% of her body weight in water
    water_intake = 54  # Nancy's daily water intake is 54 pounds

    weight = water_intake / water_intake_percentage
    result = weight
    return result

print(solution())