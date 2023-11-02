def solution():
    total_guests = 200  # Total number of guests at the party
    women_percent = 0.4  # Percentage of guests that are women
    women_count = total_guests * women_percent  # Number of women at the party
    women_rabbit_ears_percent = 0.8  # Percentage of women wearing rabbit ears
    women_rabbit_ears_count = women_count * women_rabbit_ears_percent  # Number of women wearing rabbit ears
    men_count = total_guests - women_count  # Number of men at the party
    men_rabbit_ears_percent = 0.6  # Percentage of men wearing rabbit ears
    men_rabbit_ears_count = men_count * men_rabbit_ears_percent  # Number of men wearing rabbit ears

    # Total number of people wearing rabbit ears
    total_rabbit_ears = women_rabbit_ears_count + men_rabbit_ears_count
    result = total_rabbit_ears
    return result

print(solution())