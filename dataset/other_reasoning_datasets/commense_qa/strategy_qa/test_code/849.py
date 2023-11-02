def solution():
    haiku_rules = {"length": "very short", "phrases": 3}
    book_rules = {"length": "longer than haiku", "phrases": ">3"}
    if haiku_rules["length"] == book_rules["length"] and haiku_rules["phrases"] == book_rules["phrases"]:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())