def solution():
    num_kids_soccer_pm = 750

    # Calculate the total number of kids in soccer camp
    num_kids_soccer = num_kids_soccer_pm * 2

    # Calculate the number of kids in soccer camp in the morning
    num_kids_soccer_am = num_kids_soccer / 4

    # Calculate the total number of kids in camp
    total_kids = num_kids_soccer + num_kids_soccer_am
    result = total_kids
    return result

print(solution())