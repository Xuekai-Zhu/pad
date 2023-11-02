def solution():
    goddess_name = "Friday"
    goddess_association = "Freya"
    feline_haters = ["none", "unknown"] # list of possible feline haters
    if goddess_association == "Freya" and goddess_name not in feline_haters:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())