def solution():
    saved_sep = 29
    saved_oct = 25
    saved_nov = 31
    spent_hugo = 75

    total_saved = saved_sep + saved_oct + saved_nov
    total_left = total_saved - spent_hugo
    result = total_left
    return result

print(solution())