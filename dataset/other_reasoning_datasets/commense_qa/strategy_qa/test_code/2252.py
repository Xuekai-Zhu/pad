def solution():
    wednesday_related_to_thor = False
    if "Odin" in "Wednesday" or "Wodan" in "Wednesday":
        wednesday_related_to_thor = True
    if wednesday_related_to_thor:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())