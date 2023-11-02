def solution():
    # Calculate the total amount of water needed for both Violet and her dog
    total_water_needed_per_hour = 800 + 400  # ml
    total_water_needed = total_water_needed_per_hour * hours_hiked  # ml

    # Calculate the number of hours Violet and her dog can hike with 4.8 L of water
    hours_hiked = (4.8 * 1000) / total_water_needed  # convert L to ml

    result = hours_hiked
    return result

print(solution())