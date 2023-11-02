def solution():
    people = 5
    desired_portion = 1 #lb
    ounces_per_pound = 16
    ounces_per_steak = 20
    steaks_needed = people * desired_portion * ounces_per_pound / ounces_per_steak
    result = steaks_needed
    return result

print(solution())