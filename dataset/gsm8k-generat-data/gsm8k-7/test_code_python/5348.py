def solution():
    feet_to_inches = 12 #1 ft equals 12 inches
    length = 10 #in feet
    width = 10 #in feet

    # Calculate the total area in square feet
    total_area_ft = length * width

    # Convert the area to square inches
    total_area_inches = total_area_ft * feet_to_inches * feet_to_inches

    result = total_area_inches
    return result

print(solution())