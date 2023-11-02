def solution():
    """Beth is a scuba diver.  She is excavating a sunken ship off the coast of a small Caribbean island and she must remain underwater for long periods.  Her primary tank, which she wears when she first enters the water, has enough oxygen to allow her to stay underwater for 2 hours.  She also has several 1-hour supplemental tanks that she takes with her as well as stores on the ocean floor so she can change tanks underwater without having to come up to the surface.  She will need to be underwater for 8 hours.  How many supplemental tanks will she need?"""
    # Define the number of hours the primary tank can provide oxygen
    PRIMARY_TANK_HOURS = 2

    # Define the number of hours in each supplemental tank
    SUPPLEMENTAL_TANK_HOURS = 1

    # Define the total number of hours Beth needs to be underwater
    TOTAL_HOURS_UNDERWATER = 8

    # Calculate the total number of supplemental tank hours needed
    supplemental_tank_hours_needed = TOTAL_HOURS_UNDERWATER - PRIMARY_TANK_HOURS

    # Calculate the total number of supplemental tanks needed
    supplemental_tanks_needed = supplemental_tank_hours_needed // SUPPLEMENTAL_TANK_HOURS

    # Display the number of supplemental tanks needed
    result = supplemental_tanks_needed
    return result

print(solution())