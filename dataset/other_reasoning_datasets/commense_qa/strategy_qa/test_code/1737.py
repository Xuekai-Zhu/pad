def solution():
    jpeg_stand_for = "Joint Photographic Experts Group"
    is_jpeg_joint_committee = False
    if "joint" in jpeg_stand_for.lower():
        is_jpeg_joint_committee = True
    if is_jpeg_joint_committee:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())