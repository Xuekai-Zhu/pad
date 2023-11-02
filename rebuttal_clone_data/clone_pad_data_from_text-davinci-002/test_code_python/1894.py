def solution():
    hours_needed = 32
    hours_per_poodle = 2
    hours_per_chihuahua = 1
    hours_per_labrador = 3
    monday_time = 4 * hours_per_poodle + 2 * hours_per_chihuahua
    tuesday_time = 2 * hours_per_chihuahua
    wednesday_time = 4 * hours_per_labrador
    time_needed_for_poodles = hours_needed - (monday_time + tuesday_time + wednesday_time)
    poodles_needed = time_needed_for_poodles / hours_per_poodle
    result = poodles_needed
    return result

print(solution())