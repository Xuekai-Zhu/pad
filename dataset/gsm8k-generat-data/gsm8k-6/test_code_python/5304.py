def solution():
    # Calculate the total water intake from Monday, Tuesday, Thursday, Friday, and Saturday
    total_water_intake = 9 * 3 + 8 * 3  # Gumball drank 9 liters of water on Monday, Thursday, and Saturday, and 8 liters on Tuesday, Friday, and Sunday
    # Calculate the water intake for Wednesday
    water_intake_on_Wednesday = 60 - total_water_intake  # Gumball drank 60 liters of water for the week, so the water intake on Wednesday is the difference
    result = water_intake_on_Wednesday
    return result

print(solution())