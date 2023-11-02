def solution():
    is_puerto_rico_DC = False
    is_puerto_rico_state = False
    was_23rd_amendment_for_puerto_rico = False
    if not is_puerto_rico_DC and not is_puerto_rico_state and not was_23rd_amendment_for_puerto_rico:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())