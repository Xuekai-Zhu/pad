def solution():
    funeral_traditionally_somber = True
    happy_hardcore_energetic = True
    if funeral_traditionally_somber and not happy_hardcore_energetic:
        result = "no, it is not unusual"
    else:
        result = "yes, it is unusual"
    return result

print(solution())