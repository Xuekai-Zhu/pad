def solution():
    viper_room_capacity = 250
    national_diet_capacity = 700
    if viper_room_capacity <= national_diet_capacity:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())