def solution():
    hometown_guests = 5
    school_guests = 2 * hometown_guests
    sports_club_guests = hometown_guests + school_guests
    total_guests = sports_club_guests + (0.2 * (hometown_guests + school_guests + sports_club_guests))
    result = total_guests
    return result

print(solution())