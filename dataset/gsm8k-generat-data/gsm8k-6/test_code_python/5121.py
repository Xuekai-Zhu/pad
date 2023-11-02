def solution():
    total_rhinestones = 45  # total number of rhinestones needed
    bought_rhinestones = total_rhinestones/3  # number of rhinestones bought
    found_rhinestones = total_rhinestones/5  # number of rhinestones found in supplies
    remaining_rhinestones = total_rhinestones - bought_rhinestones - found_rhinestones  # number of rhinestones still needed
    result = remaining_rhinestones
    return result

print(solution())