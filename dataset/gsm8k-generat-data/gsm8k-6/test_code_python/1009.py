def solution():
    # Calculate the number of alligators on Lagoon island
    total_alligators = 2 * 15 / 0.5  # Half the alligators are male & rest are female, there are 15 adult females

    # Calculate the number of adult female alligators on Lagoon island
    adult_female_alligators = 15

    # Calculate the number of juvenile female alligators on Lagoon island
    juvenile_female_alligators = 0.4 * (total_alligators - adult_female_alligators)

    # Calculate the number of male alligators on Lagoon island
    male_alligators = total_alligators / 2

    result = male_alligators
    return result

print(solution())