def solution():
    chiquita_height = 5  # Chiquita's height in feet
    mr_martinez_height = chiquita_height + 2  # Mr. Martinez's height in feet

    # Calculate the combined height in feet
    combined_height = chiquita_height + mr_martinez_height

    # Convert the combined height to inches
    combined_height_inches = combined_height * 12

    result = combined_height_inches
    return result

print(solution())