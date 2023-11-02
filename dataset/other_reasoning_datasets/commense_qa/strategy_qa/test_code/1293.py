def solution():
    joker_first_appearance = 1940
    bart_simpson_first_appearance = 1987
    # Assuming Bart Simpson is old enough to own comics (at least 7 years old)
    if joker_first_appearance <= bart_simpson_first_appearance - 7:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())