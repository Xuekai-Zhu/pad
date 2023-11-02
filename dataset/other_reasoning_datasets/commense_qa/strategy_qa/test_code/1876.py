def solution():
    influential_killers = ["John Hinckley Jr.", "Mark David Chapman", "Robert John Bardo"]
    catcher_in_the_rye = "Catcher in the Rye"
    if catcher_in_the_rye in influential_killers:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())