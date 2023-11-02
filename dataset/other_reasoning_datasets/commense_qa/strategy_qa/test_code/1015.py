def solution():
    squidward_musical_passion = "clarinet"
    alan_greenspan_musical_passions = ["clarinet", "saxophone"]
    if squidward_musical_passion not in alan_greenspan_musical_passions:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())