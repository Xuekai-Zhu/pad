def solution():
    minutes_per_batch = 8
    hushpuppies_per_guest = 5
    total_guests = 20
    total_hushpuppies = total_guests * hushpuppies_per_guest
    hushpuppies_per_minute = 10 / minutes_per_batch
    minutes_required = total_hushpuppies / hushpuppies_per_minute
    result = minutes_required
    return result

print(solution())