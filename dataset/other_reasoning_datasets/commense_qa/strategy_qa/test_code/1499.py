def solution():
    philippines_constitution = "ratified in 1987"
    british_constitution = "collection of legal statutes, precedent, political custom and social convention"
    if "copy text" in philippines_constitution.lower() and "british constitution" in philippines_constitution.lower():
        result = "yes"
    else:
        result = "no"
    return result

print(solution())