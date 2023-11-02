def solution():
    """Ittymangnark and Kingnook are an Eskimo couple living in the most northern region of the Alaskan wilderness.  Together, they live with their child, Oomyapeck.  Every day Ittymangnark catches enough fish for the three of them to eat for the day and they split the fish equally between the three of them.  But after they have split the fish, they give Oomyapeck all of the eyes, who gives two of the eyes to his dog and eats the rest himself.  How many fish will each of them be given to eat if Oomyapeck eats 22 eyes in a day?"""
    # Define the number of eyes per fish
    EYES_PER_FISH = 2

    # Calculate the total number of fish caught
    total_fish = 3 * (22/EYES_PER_FISH + 1) # Add one fish for themselves

    # Calculate the number of fish each person gets to eat
    fish_per_person = total_fish / 3

    # Display the number of fish each person gets
    result = fish_per_person
    return result

print(solution())