def solution():
    towels_per_guest = 1
    initial_guests = 50
    second_hour_guests = initial_guests * 1.2
    third_hour_guests = second_hour_guests * 1.25
    fourth_hour_guests = third_hour_guests * 1.33
    total_guests = initial_guests + second_hour_guests + third_hour_guests + fourth_hour_guests
    total_towels = total_guests * towels_per_guest
    result = total_towels
    return result

print(solution())