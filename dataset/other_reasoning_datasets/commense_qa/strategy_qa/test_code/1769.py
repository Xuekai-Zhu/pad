def solution():
    politician_birthplace = "Callington"
    cornwall_location = "South West England"
    birthplace_location = "South East Cornwall"
    if birthplace_location in cornwall_location:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())