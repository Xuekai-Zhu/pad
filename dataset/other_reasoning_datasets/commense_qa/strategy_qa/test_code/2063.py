def solution():
    # Define the age of the chlorine water in days
    age_of_chlorine_water_days = 7
    # Check if the chlorine in the water has completely dissolved
    if age_of_chlorine_water_days >= 5:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())