def solution():
    drain_fly_colors = ["black", "grey"]
    calico_colors = ["white", "orange", "black"]
    if set(drain_fly_colors).issubset(set(calico_colors)):
        result = "yes"
    else:
        result = "no"
    return result

print(solution())