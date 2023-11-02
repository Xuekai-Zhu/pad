def solution():
    highest_rulers = ["Tsar", "King", "Queen"]
    noble_titles = ["Duke", "Prince"]
    if "Tsar" in highest_rulers and "Duke" in noble_titles:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())