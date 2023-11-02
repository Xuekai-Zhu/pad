def solution():
    mount_emei_weight = 70000
    crane_capacity = 1200000
    if crane_capacity > mount_emei_weight:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())