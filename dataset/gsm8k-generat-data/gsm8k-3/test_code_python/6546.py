def solution():
    """John has a party and invites 30 people.  Of the people he invited 20% didn't show up.  75% of the people who show up get steak and the rest get chicken.  How many people ordered chicken?"""
    # Define the number of invited people and the percentage who didn't show up
    invited = 30
    no_show_percentage = 0.2

    # Calculate the number of people who didn't show up
    no_shows = invited * no_show_percentage

    # Calculate the number of people who showed up
    showed_up = invited - no_shows

    # Calculate the number of people who ordered steak
    steak_percentage = 0.75
    steak_orders = showed_up * steak_percentage

    # Calculate the number of people who ordered chicken
    chicken_orders = showed_up - steak_orders

    # Display the number of people who ordered chicken
    result = chicken_orders
    return result

print(solution())