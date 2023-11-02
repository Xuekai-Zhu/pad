def solution():
    mentioned_bones = ["hip bone", "back bone", "knee bone"]
    connected_bones = ["back bone"]
    overlap = [bone for bone in mentioned_bones if bone in connected_bones]
    if overlap:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())