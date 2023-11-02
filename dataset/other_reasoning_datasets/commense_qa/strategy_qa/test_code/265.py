def solution():
    play_title = "No Exit"
    play_subject = "Hell"
    if play_subject.lower() in play_title.lower():
        result = "yes"
    else:
        result = "no"
    return result

print(solution())