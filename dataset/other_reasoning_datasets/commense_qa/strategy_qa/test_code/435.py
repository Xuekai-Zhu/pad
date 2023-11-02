def solution():
    # Define some relevant information
    jesuits_sent_abroad = 1598
    roman_catholic = True
    attend_mass_on_sundays = True
    # Check if the first missionaries were required to attend mass on Sundays
    if jesuits_sent_abroad <= 1598 and roman_catholic and attend_mass_on_sundays:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())