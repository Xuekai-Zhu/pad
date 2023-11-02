def solution():
    num_guests = 3 * 12  # 3 dozen guests
    num_extra_guests = num_guests / 3  # 1/3 of guests bring a guest
    num_guests -= 5  # 5 guests can't make it
    num_chairs = num_guests + num_extra_guests + 12  # add 12 extra chairs
    result = num_chairs
    return result

print(solution())