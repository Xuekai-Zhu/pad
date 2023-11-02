def solution():
    has_mental_illness = False
    reason_for_seek = ["relationship issues", "grief"]
    # Check if any of the reasons for seeking psychotherapy do not involve mental illness
    for reason in reason_for_seek:
        if reason not in ["anxiety", "depression", "personality disorders", "mood disorders"]:
            has_mental_illness = False
            break
        else:
            has_mental_illness = True
    if not has_mental_illness:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())