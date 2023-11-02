Unfortunately, the solution for the previous question (Samantha's last name) was not provided. Here is the solution for this new question:

def solution():
    """Sam sells bread. He has a target of selling 120 crates of bread in a week. One week he was closed on Monday and Friday. Over the weekend he sold 20 crates. On Tuesday he sold 15 crates, on Wednesday 12 crates, and Thursday 18 crates. By how many crates was Sam off from his target for the week?"""
    target_crates = 120
    weekend_crates = 20
    weekday_crates = 15 + 12 + 18
    closed_days = 2
    total_crates = weekend_crates + weekday_crates
    actual_crates = total_crates + (closed_days * (target_crates / 5))
    off_target = target_crates - actual_crates
    result = off_target
    return result

print(solution())