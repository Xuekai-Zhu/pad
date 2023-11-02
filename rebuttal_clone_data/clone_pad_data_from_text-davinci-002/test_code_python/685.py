def solution():
    total_kids = 750
    kids_going_to_soccer_camp = total_kids / 2
    kids_going_to_soccer_camp_in_morning = kids_going_to_soccer_camp / 4
    total_kids_going_to_soccer_camp = kids_going_to_soccer_camp + kids_going_to_soccer_camp_in_morning
    result = total_kids_going_to_soccer_camp
    return result

print(solution())