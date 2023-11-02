def solution():
    """Andrew's father buys a package of 100 masks. Andrew lives with his 2 parents and 2 siblings. All members of Andrew's family change masks every 4 days. How many days will it take to finish the pack of masks?"""
    # Define the number of people in Andrew's family
    NUM_PEOPLE = 5

    # Define the number of masks used by each person every 4 days
    MASKS_PER_PERSON = 1

    # Calculate the total number of masks used every 4 days
    total_masks_per_4_days = NUM_PEOPLE * MASKS_PER_PERSON

    # Calculate the number of 4-day periods it takes to use all the masks
    num_periods = 100 / total_masks_per_4_days

    # Calculate the total number of days it takes to use all the masks
    total_days = num_periods * 4

    # Display the total number of days
    result = total_days
    return result

print(solution())