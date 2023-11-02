def solution():
    # Define the number of people and the hours of the trip
    num_people = 4
    trip_hours = 8 * 2  # Round trip of 8 hours each way

    # Calculate the total bottles of water needed
    water_per_person_per_hour = 0.5
    total_water_needed = num_people * trip_hours * water_per_person_per_hour

    # Round up to the nearest integer
    total_water_needed = int(total_water_needed) + int(total_water_needed % 1 > 0)

    result = total_water_needed
    return result

print(solution())