def solution():
    deadly_sins = ["pride", "greed", "wrath", "envy", "lust", "gluttony", "sloth"]
    columbus_actions = ["greed", "wrath", "envy"]
    overlap = [sin for sin in deadly_sins if sin in columbus_actions]
    if overlap:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())