def solution():
    num_families = 3
    num_people_per_family = 4
    num_days = 7
    towels_per_day_per_person = 1
    towels_per_load = 14

    # Calculate the total number of towels used during the vacation
    total_towels_used = num_families * num_people_per_family * num_days * towels_per_day_per_person

    # Calculate the number of loads of laundry needed to wash all the towels
    num_laundry_loads = total_towels_used / towels_per_load

    result = num_laundry_loads
    return result

print(solution())