def solution():
    yellow_pages = "alphabetized phone listings"
    google = "type in a name quickly"
    household_ai = "speak a name and ask for number"
    if yellow_pages not in (google, household_ai):
        result = "yes"
    else:
        result = "no"
    return result

print(solution())