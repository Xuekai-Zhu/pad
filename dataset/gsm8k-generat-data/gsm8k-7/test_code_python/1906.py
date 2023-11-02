def solution():
    daily_water_intake = 54
    water_intake_percent = 0.6  # 60% of body weight

    # Calculate the total body weight of Nancy
    total_body_weight = daily_water_intake / water_intake_percent
    result = total_body_weight
    return result

print(solution())