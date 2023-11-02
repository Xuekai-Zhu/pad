def solution():
    businesses_fired_from = 36
    businesses_quit = 24
    total_businesses = 72
    businesses_can_apply_to = total_businesses - businesses_fired_from - businesses_quit
    result = businesses_can_apply_to
    return result

print(solution())