def solution():
    
    slices_per_tomato = 8
    slices_per_person = 20
    people_to_feed = 8
    total_slices_needed = slices_per_person * people_to_feed
    tomatoes_needed = total_slices_needed / slices_per_tomato
    result = tomatoes_needed
    return result

print(solution())