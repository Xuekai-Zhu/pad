def solution():
    
    sheets_per_room = 2
    pillow_cases_per_room = 2 * sheets_per_room
    towels_per_room = 2 * pillow_cases_per_room
    total_sheets = sheets_per_room * 80
    total_pillow_cases = pillow_cases_per_room * 80
    total_towels = towels_per_room * 80
    total_laundry = total_sheets + total_pillow_cases + total_towels
    result = total_laundry
    return result

print(solution())