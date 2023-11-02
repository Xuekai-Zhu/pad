def solution():
    """John has a party and invites 30 people. Of the people he invited 20% didn't show up. 75% of the people who show up get steak and the rest get chicken. How many people ordered chicken?"""
    # Define the number of people invited to the party
    total_invited = 30

    # Calculate the number of people who didn't show up
    no_show = total_invited * 0.2

    # Calculate the number of people who actually showed up
    total_attendees = total_invited - no_show

    # Calculate the number of people who ordered steak
    steak_orders = total_attendees * 0.75

    # Calculate the number of people who ordered chicken
    chicken_orders = total_attendees - steak_orders

    # return the result
    result = chicken_orders
    return result

print(solution())