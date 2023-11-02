def solution():
    smallest_bones = ["malleus", "incus", "stapes"]
    largest_bone = "femur"
    torso_location = "center"
    if largest_bone in torso_location and all(bone not in torso_location for bone in smallest_bones):
        result = "yes"
    else:
        result = "no"
    return result

print(solution())