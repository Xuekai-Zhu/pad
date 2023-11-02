def solution():
    is_margarine_dairy_free = True
    is_veganism_dairy_free = True
    if is_margarine_dairy_free and is_veganism_dairy_free:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())