def solution():
    mushrooms_used_for = ["providing extra lives", "making Mario grow"]
    run_faster_items = ["bunny ears", "starman"]
    if "running faster" in mushrooms_used_for:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())