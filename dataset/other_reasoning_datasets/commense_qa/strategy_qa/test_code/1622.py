def solution():
    traditional_watch_parts = ["coils", "springs", "gears", "metal parts"]
    apple_watch_parts = ["computer", "wireless technology"]
    if set(traditional_watch_parts).issubset(set(apple_watch_parts)):
        result = "no"
    else:
        result = "yes"
    return result

print(solution())