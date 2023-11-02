def solution():
    # Define information about Opal Tometi and the Ku Klux Klan
    opal_tometi_race = "African American"
    kkk_targets = ["African Americans", "Jews", "immigrants", "leftists", "homosexuals"]
    # Check if Opal Tometi fits the profile of those targeted by the KKK
    if opal_tometi_race in kkk_targets:
        result = "no"
    else:
        result = "unknown"
    return result

print(solution())