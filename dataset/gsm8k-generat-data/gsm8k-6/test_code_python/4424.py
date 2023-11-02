def solution():
    # Calculate the number of male and female guests
    female_guests = 0.4 * 200  # 40% of the guests are women
    male_guests = 200 - female_guests

    # Calculate the number of guests wearing rabbit ears
    female_rabbit_ears = 0.8 * female_guests  # 80% of the women are wearing rabbit ears
    male_rabbit_ears = 0.6 * male_guests  # 60% of the males are wearing rabbit ears
    total_rabbit_ears = female_rabbit_ears + male_rabbit_ears

    result = total_rabbit_ears
    return result

print(solution())