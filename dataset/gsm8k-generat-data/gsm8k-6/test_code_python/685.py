def solution():
    # Calculate number of kids going to soccer camp in the morning
    morning_soccer_camp = (1/4) * (1/2) * total_kids

    # Calculate total number of kids in soccer camp
    total_soccer_camp = (1/2) * total_kids

    # Calculate total number of kids in camp using afternoon soccer camp numbers
    total_kids = 750 * 2

    # Calculate total number of kids in camp
    total_kids = total_soccer_camp + morning_soccer_camp + 750
    result = total_kids
    return result

print(solution())