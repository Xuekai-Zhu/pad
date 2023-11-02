def solution():
    # Calculate the percentage of ads that are blocked
    blocked_percent = 80

    # Calculate the percentage of ads that aren't blocked
    not_blocked_percent = 100 - blocked_percent

    # Calculate the percentage of ads that are both not blocked and not interesting
    not_interesting_percent = not_blocked_percent * 0.8

    # Calculate the percentage of ads that aren't interesting but may or may not be blocked
    not_interesting_maybe_blocked_percent = blocked_percent * 0.2

    # Calculate the final percentage of ads that aren't interested and don't get blocked
    not_interesting_not_blocked_percent = not_interesting_percent + not_interesting_maybe_blocked_percent

    result = not_interesting_not_blocked_percent
    return result

print(solution())