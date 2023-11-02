def solution():
    # Calculate the number of female guests
    num_female = 0.4 * 200

    # Calculate the number of female guests wearing rabbit ears
    num_female_with_ears = 0.8 * num_female

    # Calculate the number of male guests
    num_male = 200 - num_female

    # Calculate the number of male guests wearing rabbit ears
    num_male_with_ears = 0.6 * num_male

    # Calculate the total number of guests wearing rabbit ears
    total_with_ears = num_female_with_ears + num_male_with_ears

    result = total_with_ears
    return result

print(solution())