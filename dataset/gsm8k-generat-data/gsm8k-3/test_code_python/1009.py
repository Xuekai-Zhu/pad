def solution():
    """Lagoon island is populated by alligators. Half the alligators are male. The rest are female. Among the females, 40% are juveniles. There are 15 adult females. How many male alligators are there?"""
    # Define the proportion of male alligators
    MALE_PROPORTION = 0.5

    # Define the proportion of female alligators
    FEMALE_PROPORTION = 1 - MALE_PROPORTION

    # Calculate the total number of alligators
    total_alligators = 15 / FEMALE_PROPORTION

    # Calculate the number of female juveniles
    female_juveniles = 0.4 * (total_alligators * FEMALE_PROPORTION)

    # Calculate the number of adult female alligators
    adult_females = 15

    # Calculate the number of male alligators
    male_alligators = (total_alligators * MALE_PROPORTION) - ((total_alligators * FEMALE_PROPORTION) - female_juveniles) - adult_females

    # Display the number of male alligators
    result = male_alligators
    return result

print(solution())