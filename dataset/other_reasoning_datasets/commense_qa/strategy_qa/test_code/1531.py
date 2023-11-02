def solution():
    fingers_per_hand = 4
    fingers_needed_to_count_five = 5
    if fingers_needed_to_count_five <= fingers_per_hand:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())