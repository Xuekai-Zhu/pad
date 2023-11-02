def solution():
    """At a James Bond movie party, each guest is either male (M) or female (F. 40% of the guests are women, 80% of the women are wearing rabbit ears, and 60% of the males are wearing rabbit ears. If the total number of guests at the party is 200, given all this information, what is the total number of people wearing rabbit ears?"""
    # Define the total number of guests and the percentage of women
    total_guests = 200
    women_percentage = 0.4

    # Calculate the number of women and men
    women_count = total_guests * women_percentage
    men_count = total_guests - women_count

    # Calculate the number of women wearing rabbit ears
    women_rabbit_count = women_count * 0.8

    # Calculate the number of men wearing rabbit ears
    men_rabbit_count = men_count * 0.6

    # Calculate the total number of guests wearing rabbit ears
    total_rabbit_count = women_rabbit_count + men_rabbit_count

    # Return the result
    result = total_rabbit_count
    return result

print(solution())