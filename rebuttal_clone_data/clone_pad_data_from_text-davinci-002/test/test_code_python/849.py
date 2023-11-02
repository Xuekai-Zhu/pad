def solution():
    initial_bones = 4
    bones_gained = initial_bones
    bones_lost = 2
    net_gain = bones_gained - bones_lost
    final_bone_count = initial_bones + net_gain
    result = final_bone_count
    return result

print(solution())