def solution():
    weekday = "Wednesday"
    camel_anatomy = "hump"
    if weekday.lower() == "wednesday" and camel_anatomy.lower() in weekday.lower():
        result = "yes"
    else:
        result = "no"
    return result

print(solution())