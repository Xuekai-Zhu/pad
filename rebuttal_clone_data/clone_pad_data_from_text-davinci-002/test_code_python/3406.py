def solution():
    rooms_for_couples = 13
    rooms_for_singles = 14
    total_rooms = rooms_for_couples + rooms_for_singles
    baths_for_couples = 2
    baths_for_singles = 1
    total_baths = baths_for_couples + baths_for_singles
    bubble_bath_needed = total_baths * total_rooms * 10
    result = bubble_bath_needed
    return result

print(solution())