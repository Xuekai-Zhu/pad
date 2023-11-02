def solution():
    human_sacrum_fused_vert = 5
    malamute_sacrum_fused_vert = 3
    if human_sacrum_fused_vert > malamute_sacrum_fused_vert:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())