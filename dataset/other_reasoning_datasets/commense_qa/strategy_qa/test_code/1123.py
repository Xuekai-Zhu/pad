def solution():
    cartoon_character = "dog"
    dog_bone_brand = "Nylabone"
    reasons_dogs_chew_bones = ["taste", "exercise jaw muscles"]
    if cartoon_character == "dog" and dog_bone_brand == "Nylabone" and all(reason in reasons_dogs_chew_bones for reason in reasons_dogs_chew_bones):
        result = "yes"
    else:
        result = "no"
    return result

print(solution())