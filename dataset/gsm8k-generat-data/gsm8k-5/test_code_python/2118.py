def solution():
    total_businesses = 72
    businesses_fired_from = total_businesses / 2
    businesses_quit_from = total_businesses / 3

    # Calculate the remaining businesses that Brandon can apply to
    remaining_businesses = total_businesses - businesses_fired_from - businesses_quit_from
    result = remaining_businesses
    return result

print(solution())