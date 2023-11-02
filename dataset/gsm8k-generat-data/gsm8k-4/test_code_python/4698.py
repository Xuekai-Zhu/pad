def solution():
    """Andrew's father buys a package of 100 masks. Andrew lives with his 2 parents and 2 siblings. All members of Andrew's family change masks every 4 days. How many days will it take to finish the pack of masks?"""
    # Define the number of family members
    family_members = 5

    # Define the number of masks in the package
    masks_in_package = 100

    # Calculate the number of masks used per day
    masks_per_day = family_members / 4

    # Calculate the number of days it will take to finish the package
    days_to_finish = masks_in_package / masks_per_day

    result = days_to_finish
    return result

print(solution())