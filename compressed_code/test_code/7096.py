def solution():
    
    initial_papayas = 14
    friday_yellow = 2
    sunday_yellow = 2 * friday_yellow
    remaining_papayas = initial_papayas - (friday_yellow + sunday_yellow)
    result = remaining_papayas
    return result

print(solution())