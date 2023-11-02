def solution():
    """Lagoon island is populated by alligators. Half the alligators are male. The rest are female. Among the females, 40% are juveniles. There are 15 adult females. How many male alligators are there?"""
    # Define the total number of alligators
    total_alligators = None

    # Define the number of female alligators
    female_alligators = None

    # Define the number of male alligators
    male_alligators = None

    # Define the number of juvenile female alligators
    juvenile_females = None

    adult_females = 15

    # Calculate the total number of alligators
    total_alligators = female_alligators = 2 * adult_females

    # Calculate the number of juvenile females
    juvenile_females = female_alligators * 0.4

    # Calculate the number of male alligators
    male_alligators = total_alligators - female_alligators

    result = male_alligators
    return result

print(solution())