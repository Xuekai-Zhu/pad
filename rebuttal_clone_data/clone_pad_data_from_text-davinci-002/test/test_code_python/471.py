def solution():
    # 7 things to do to clean the house
    # 1 thing to do to take a shower
    # 4 things to do to make dinner
    total_things_to_do = 7 + 1 + 4
    time_per_thing = 10
    total_time = total_things_to_do * time_per_thing
    hours = total_time / 60
    result = hours
    return result

print(solution())