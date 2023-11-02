def solution():
    holiday = "Passover"
    eaten_part = "tibia"
    holiday_food = ["goat shank", "parsley"]
    if holiday == "Passover" and eaten_part in holiday_food:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())