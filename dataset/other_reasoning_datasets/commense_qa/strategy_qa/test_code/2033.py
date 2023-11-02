def solution():
    has_psychotic_episodes = True
    has_delusions = True
    if has_psychotic_episodes and has_delusions:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())