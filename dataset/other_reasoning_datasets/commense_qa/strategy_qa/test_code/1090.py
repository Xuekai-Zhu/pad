def solution():
    location = "New York Harbor"
    object = "Statue of Liberty"
    description = "very large, green statue of a woman"
    if location == "New York Harbor" and object == "Statue of Liberty" and "green" in description.lower():
        result = "yes"
    else:
        result = "no"
    return result

print(solution())