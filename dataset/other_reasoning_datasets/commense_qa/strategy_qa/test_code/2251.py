def solution():
    royal_family_members = ["Queen Elizabeth II", "Prince Andrew"]
    alleged_felonies = ["sexual assault"]
    # Check if any royal family member has been accused of a felony
    for member in royal_family_members:
        if member == "Prince Andrew" and alleged_felonies:
            result = "yes"
            break
        else:
            result = "no"
    return result

print(solution())