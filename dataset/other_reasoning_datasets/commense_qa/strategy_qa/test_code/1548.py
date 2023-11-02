def solution():
    doctor_number = 10
    doctor_actor = "David Tennant"
    doctor_likes_pears = False
    dish_name = "stuffed pears"
    if doctor_number == 10 and doctor_actor == "David Tennant" and not doctor_likes_pears and dish_name.lower().startswith("pear"):
        result = "no"
    else:
        result = "yes"
    return result

print(solution())