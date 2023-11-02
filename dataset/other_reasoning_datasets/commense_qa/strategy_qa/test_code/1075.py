def solution():
    pandora_ills = ["famine", "sickness", "death"]
    horsemen = ["pestilence", "war", "famine", "death"]
    overlap = [item for item in pandora_ills if item in horsemen]
    if len(overlap) >= 2:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())