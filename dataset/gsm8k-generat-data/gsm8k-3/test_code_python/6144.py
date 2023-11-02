def solution():
    """20 kids in preschool are ready for a nap.  1/2 of the kids fall asleep within the first 5 minutes.  Then half of the kids remaining fall asleep within another 5 minutes.  How many kids are still awake?"""
    # Define the number of kids in preschool
    kids = 20

    # Half of the kids fall asleep within the first 5 minutes
    kids_asleep_1 = kids / 2

    # Half of the remaining kids fall asleep within the next 5 minutes
    kids_asleep_2 = kids_asleep_1 / 2

    # Calculate the number of kids still awake
    kids_awake = kids - kids_asleep_1 - kids_asleep_2

    # Display the number of kids still awake
    result = kids_awake
    return result

print(solution())