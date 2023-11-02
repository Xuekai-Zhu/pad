def solution():
    invited_guests = 3 * 12  # Thomas invites 3 dozen guests, or 36 guests
    extra_guests = invited_guests // 3  # 1/3 of the guests bring an extra guest
    total_guests = invited_guests + extra_guests  # Thomas needs chairs for all the guests
    total_guests -= 5  # 5 guests can't make it
    total_chairs = total_guests + 12  # Thomas orders 12 extra chairs

    result = total_chairs
    return result

print(solution())