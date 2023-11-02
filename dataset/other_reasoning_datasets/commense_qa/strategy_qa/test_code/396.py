def solution():
    before = "no"
    after = "no"
    # Check if a woman was Prime Minister directly before Stanley Baldwin
    if before == "yes":
        result = "before"
    # Check if a woman was Prime Minister directly after Stanley Baldwin
    elif after == "yes":
        result = "after"
    else:
        result = "neither"
    return result

print(solution())