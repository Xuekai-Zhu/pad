def solution():
    main_character = "Alice"
    minimum_age = 18
    is_female = True
    if main_character != "Alice" and minimum_age <= 21 and not is_female:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())