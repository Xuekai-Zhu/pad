def solution():
    collaborators = ["Staple Singers", "Jerry Butler", "Aretha Franklin", "the Impressions", "Curtis Mayfield"]
    suicidal_person = "Donny Hathaway"
    if suicidal_person in collaborators:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())