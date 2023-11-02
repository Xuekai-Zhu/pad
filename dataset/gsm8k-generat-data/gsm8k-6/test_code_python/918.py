def solution():
    # Calculate the area of the house and the porch
    area_house = 20.5 * 10  # area of the house
    area_porch = 6 * 4.5  # area of the porch
    total_area = area_house + area_porch  # total area to be covered with shingles

    # Calculate the amount of shingles needed
    shingles_needed = total_area / 100  # assuming each shingle covers 100 square feet

    result = shingles_needed
    return result

print(solution())