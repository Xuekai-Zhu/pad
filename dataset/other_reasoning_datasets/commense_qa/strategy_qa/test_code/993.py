def solution():
    # Define the relationships between Lionel Richie, Nicole Richie, and Sheila E
    lionel_is_adoptive_parent = True
    nicole_is_raised_by_lionel = True
    nicole_is_niece_of_sheila_e = True
    # Check if Lionel Richie is related to Sheila E
    if lionel_is_adoptive_parent and nicole_is_raised_by_lionel and nicole_is_niece_of_sheila_e:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())