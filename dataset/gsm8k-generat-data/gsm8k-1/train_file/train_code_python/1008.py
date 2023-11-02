def solution():
    """Lagoon island is populated by alligators. Half the alligators are male. The rest are female. Among the females, 40% are juveniles. There are 15 adult females. How many male alligators are there?"""
    total_alligators = 2 * 15  # since half are male
    female_alligators = total_alligators - 15  # subtracting adult females to get only females
    juvenile_females = 0.4 * female_alligators
    adult_females = 15
    male_alligators = total_alligators - (juvenile_females + adult_females)
    result = male_alligators
    return result

print(solution())