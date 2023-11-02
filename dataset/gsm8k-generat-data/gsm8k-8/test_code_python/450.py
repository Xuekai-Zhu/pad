def solution():
    # Calculate the total gallons of milk Flora needs to drink in 3 weeks
    total_gallons = 105

    # Calculate how many gallons Flora needs to drink daily to meet Dr. Juan's requirement
    daily_gallons_needed = total_gallons / 21

    # Calculate how many more gallons Flora needs to drink daily than her initial plan of 3 gallons
    additional_gallons_needed = daily_gallons_needed - 3

    result = additional_gallons_needed
    return result

print(solution())