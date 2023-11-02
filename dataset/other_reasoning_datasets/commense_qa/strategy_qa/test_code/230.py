def solution():
    target_group = "Muslims"
    individual = "Donald Trump"
    if target_group not in individual:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())