def solution():
    """It takes 20 minutes for the oil to heat up to 300 degrees. It then takes 40% longer for the oil to heat up to the desired temperature of 400 degrees. After warming the oil it takes 5 minutes less time to cook than it took to warm up the oil. How much time passes from starting the oil to having cooked chicken?"""
    oil_heatup_time = 20
    heating_time_increase = oil_heatup_time * 0.4
    oil_desired_temp_time = oil_heatup_time + heating_time_increase
    oil_cook_time = oil_desired_temp_time - 5
    total_time = oil_heatup_time + oil_desired_temp_time + oil_cook_time
    result = total_time
    return result

print(solution())