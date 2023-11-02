def solution():
    # Define the presence of alcoholism-related trauma triggers in Rick and Morty
    rick_alcoholism = True
    morty_alcoholism = False
    beth_alcoholism = True
    # Check if Rick and Morty could be triggered as children of alcoholics
    if rick_alcoholism or beth_alcoholism:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())