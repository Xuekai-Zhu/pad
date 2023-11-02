def solution():
    """At a James Bond movie party, each guest is either male (M) or female (F. 40% of the guests are women, 80% of the women are wearing rabbit ears, and 60% of the males are wearing rabbit ears. If the total number of guests at the party is 200, given all this information, what is the total number of people wearing rabbit ears?"""
    # Get the total number of guests
    total_guests = 200

    # Calculate the number of women and men
    women = int(total_guests * 0.4)
    men = total_guests - women

    # Calculate the number of women wearing rabbit ears
    women_with_ears = int(women * 0.8)

    # Calculate the number of men wearing rabbit ears
    men_with_ears = int(men * 0.6)

    # Calculate the total number of people wearing rabbit ears
    total_with_ears = women_with_ears + men_with_ears

    result = total_with_ears
    return result

print(solution())