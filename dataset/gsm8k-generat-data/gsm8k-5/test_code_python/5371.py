def solution():
    total_apples = 20  # Martha has 20 apples
    jane_apples = 5  # Jane got 5 apples
    james_apples = jane_apples + 2  # James got 2 more apples than Jane
    apples_given = jane_apples + james_apples  # Total apples given away
    apples_left = total_apples - apples_given  # Apples left after giving away

    # Calculate how many more apples Martha needs to give away to be left with only 4
    additional_apples = apples_left - 4
    result = additional_apples
    return result

print(solution())