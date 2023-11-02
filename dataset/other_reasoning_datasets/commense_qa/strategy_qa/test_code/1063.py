def solution():
    pirates_suffered_from_scurvy = True
    scurvy_caused_by_lack_of_vitaminC = True
    if pirates_suffered_from_scurvy and scurvy_caused_by_lack_of_vitaminC:
        result = "yes, pirates who had scurvy needed more Vitamin C"
    else:
        result = "no, if pirates had scurvy it means they lacked Vitamin C"
    return result

print(solution())