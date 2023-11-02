def solution():
    is_historical_fiction = True
    is_popular_science = False
    if is_historical_fiction and not is_popular_science:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())