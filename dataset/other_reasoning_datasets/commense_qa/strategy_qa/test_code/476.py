def solution():
    # Check if Kurt Cobain struggled with mental health and suicide
    struggled_with_mental_health = True
    struggled_with_suicide = True
    # Check if Kurt Cobain could have benefited from Project Semicolon
    if struggled_with_mental_health and struggled_with_suicide:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())