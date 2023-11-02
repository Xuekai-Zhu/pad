def solution():
    is_in_favor = False
    if "Better Together" in campaign_name:
        is_in_favor = True
    if is_in_favor:
        result = "no"
    else:
        result = "unknown"
    return result

print(solution())