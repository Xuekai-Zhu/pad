def solution():
    """At a James Bond movie party, each guest is either male (M) or female (F. 40% of the guests are women, 80% of the women are wearing rabbit ears, and 60% of the males are wearing rabbit ears. If the total number of guests at the party is 200, given all this information, what is the total number of people wearing rabbit ears?"""
    total_guests = 200
    female_percentage = 0.4
    females = int(total_guests * female_percentage)
    males = total_guests - females
    female_rabbit_percentage = 0.8
    male_rabbit_percentage = 0.6
    females_wearing_rabbit_ears = int(females * female_rabbit_percentage)
    males_wearing_rabbit_ears = int(males * male_rabbit_percentage)
    total_wearing_rabbit_ears = females_wearing_rabbit_ears + males_wearing_rabbit_ears
    result = total_wearing_rabbit_ears
    return result

print(solution())