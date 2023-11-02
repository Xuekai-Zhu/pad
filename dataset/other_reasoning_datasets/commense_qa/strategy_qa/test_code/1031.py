def solution():
    involved_airlines = ["Boeing", "Pan Am", "United Airlines"]
    if "United Airlines" not in involved_airlines:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())