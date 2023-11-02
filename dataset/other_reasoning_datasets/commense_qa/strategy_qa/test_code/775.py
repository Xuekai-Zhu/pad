def solution():
    hippo_size = "large"
    hippo_teeth = "large"
    threatened = True
    if (hippo_size == "large" and hippo_teeth == "large") or threatened:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())