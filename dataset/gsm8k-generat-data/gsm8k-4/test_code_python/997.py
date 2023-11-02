def solution():
    """Ittymangnark and Kingnook are an Eskimo couple living in the most northern region of the Alaskan wilderness.
    Together, they live with their child, Oomyapeck. Every day Ittymangnark catches enough fish for the three
    of them to eat for the day and they split the fish equally between the three of them. But after they have
    split the fish, they give Oomyapeck all of the eyes, who gives two of the eyes to his dog and eats
    the rest himself. How many fish will each of them be given to eat if Oomyapeck eats 22 eyes in a day?"""
    # Define the number of eyes in a fish
    EYES_PER_FISH = 2

    # Calculate the total number of eyes from the fish they eat in a day
    total_eyes = EYES_PER_FISH * 3

    # Subtract the number of eyes Oomyapeck eats to find the number of eyes to be split between Ittymangnark and Kingnook
    eyes_to_split = total_eyes - 22

    # Divide the remaining eyes by the number of people to find the number of eyes each person gets
    eyes_per_person = eyes_to_split / 2

    # Add the number of eyes per person to the number of eyes per fish to find the total number of eyes and fish per person
    total_per_person = EYES_PER_FISH + eyes_per_person

    result = round(total_per_person)
    return result

print(solution())