def solution():
    
    total_guests = 36
    hotdogs_needed = total_guests / 2
    guests_with_second_hotdog = 40
    guests_without_second_hotdog = total_guests - hotdogs_needed - guests_with_second_hotdog
    result = guests_without_second_hotdog
    return result

print(solution())