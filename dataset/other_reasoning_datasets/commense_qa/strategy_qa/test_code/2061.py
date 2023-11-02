def solution():
    commandment = "Thou Shalt Not Kill"
    columbus_actions = "ordered a brutal crackdown in which many natives were killed, and then paraded their dismembered bodies through the streets"
    if commandment in columbus_actions:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())