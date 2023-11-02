def solution():
    chairs_per_guest = 1
    original_guests = 3 * 12
    additional_guests = original_guests / 3
    guests_who_cant_make_it = 5
    total_guests = original_guests + additional_guests - guests_who_cant_make_it
    chairs_to_order = total_guests * chairs_per_guest + 12
    result = chairs_to_order
    return result

print(solution())