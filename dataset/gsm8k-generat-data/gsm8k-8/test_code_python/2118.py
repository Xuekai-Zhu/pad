def solution():
    # Calculate the number of businesses Brandon has been fired from
    fired_from = 72 * 0.5

    # Calculate the number of businesses Brandon has quit from
    quit_from = 72 * (1/3)

    # Calculate the total number of businesses Brandon can no longer apply to
    cannot_apply = fired_from + quit_from

    # Calculate the total number of businesses Brandon can still apply to
    can_apply = 72 - cannot_apply
    result = can_apply
    return result

print(solution())