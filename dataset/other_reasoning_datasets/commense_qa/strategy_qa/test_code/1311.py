def solution():
    nordic_countries = ["Denmark", "Sweden", "Norway", "Finland", "Iceland"]
    japan = "Japan"
    if japan not in nordic_countries:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())