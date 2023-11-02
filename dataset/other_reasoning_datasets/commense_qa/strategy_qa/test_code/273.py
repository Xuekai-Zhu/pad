def solution():
    required_body_parts = ["arms", "legs", "other"]
    required_bones = ["tibia"]
    overlap = [part for part in required_body_parts if part in required_bones]
    if overlap:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())