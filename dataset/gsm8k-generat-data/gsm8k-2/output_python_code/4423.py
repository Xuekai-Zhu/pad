def solution():
    """At a James Bond movie party, each guest is either male (M) or female (F). 40% of the guests are women,
    80% of the women are wearing rabbit ears, and 60% of the males are wearing rabbit ears. If the total number of guests
    at the party is 200, given all this information, what is the total number of people wearing rabbit ears?"""
    total_guests = 200
    women_percentage = 40/100
    women_total = women_percentage * total_guests
    women_with_rabbit_ears = 80/100 * women_total
    men_total = total_guests - women_total
    men_with_rabbit_ears = 60/100 * men_total
    total_with_rabbit_ears = women_with_rabbit_ears + men_with_rabbit_ears
    result = total_with_rabbit_ears
    return result

print(solution())