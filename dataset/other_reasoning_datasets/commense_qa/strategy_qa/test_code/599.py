def solution():
    robert_plant_band = ["Led Zepplin", "The Honeydrippers"]
    ernest_chataway_band = ["The Honeydrippers"]
    overlap = [member for member in robert_plant_band if member in ernest_chataway_band]
    if overlap:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())