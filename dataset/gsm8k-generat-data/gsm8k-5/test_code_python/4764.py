def solution():
    current_water_intake = 15  # Happy currently drinks 15 cups of water every week
    increase_percent = 40  # Happy needs to increase her water intake by 40%
    recommended_water_intake = current_water_intake * (1 + increase_percent/100)  # Calculate the recommended water intake

    result = recommended_water_intake
    return result

print(solution())