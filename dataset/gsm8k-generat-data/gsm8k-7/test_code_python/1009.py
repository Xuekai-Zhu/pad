def solution():
    total_alligators = 2 * 15  # Half of the alligators are male
    num_female_alligators = total_alligators - 15  # Subtract the 15 adult females to get the number of non-adult females

    num_juvenile_females = round(num_female_alligators * 0.4)  # Calculate the number of juvenile females (using rounding)
    num_adult_females = 15  # Given in the problem

    num_male_alligators = total_alligators - num_female_alligators  # Calculate the number of male alligators
    result = num_male_alligators
    return result

print(solution())