def solution():
    requires_pollination = True
    seedless = True
    entomophobia = True
    if not requires_pollination and seedless and entomophobia:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())