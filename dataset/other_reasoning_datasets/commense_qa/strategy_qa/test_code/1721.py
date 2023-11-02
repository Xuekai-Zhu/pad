def solution():
    # Determine if snake venom could harm an android
    android_composition = "wires and computer parts"
    if android_composition != "biological tissue":
        result = "no"
    else:
        result = "yes"
    return result

print(solution())