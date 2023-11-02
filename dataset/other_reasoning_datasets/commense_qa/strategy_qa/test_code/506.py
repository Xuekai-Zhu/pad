def solution():
    morris_county_was_named_after = "Colonel Lewis Morris"
    was_named_after_chief_justice = True
    if "chief justice" in morris_county_was_named_after.lower() and was_named_after_chief_justice:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())