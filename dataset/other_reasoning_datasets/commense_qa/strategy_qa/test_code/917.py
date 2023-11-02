def solution():
    space_race = ["USA", "USSR"]
    athletic_event = "relay race"
    equipment_needed = "relay baton"
    if athletic_event in space_race and equipment_needed in space_race:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())