def solution():
    marvel_villains = ["Thanos", "Magneto", "Green Goblin", "Doctor Octopus", "Mandarin"]
    citrus_fruits = ["orange", "lemon", "lime", "mandarin"]
    overlap = [villain for villain in marvel_villains if villain in citrus_fruits]
    if overlap:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())