def solution():
    ideal_texture = "soft and easily chewed"
    if ideal_texture not in "tough and rubbery":
        result = "yes, shrimp do not taste best when cooked for a long time"
    else:
        result = "no, shrimp do not taste best when cooked for a long time"
    return result

print(solution())