def solution():
    neck_complications = ["stroke", "paralysis"]
    lower_back_complications = ["herniated disks"]
    dangerous_manipulations = neck_complications + lower_back_complications
    if dangerous_manipulations:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())