def solution():
    """Beth is a scuba diver. She is excavating a sunken ship off the coast of a small Caribbean island and she must remain underwater for long periods. Her primary tank, which she wears when she first enters the water, has enough oxygen to allow her to stay underwater for 2 hours. She also has several 1-hour supplemental tanks that she takes with her as well as stores on the ocean floor so she can change tanks underwater without having to come up to the surface. She will need to be underwater for 8 hours. How many supplemental tanks will she need?"""
    # Define the length of time Beth can stay underwater with the primary tank
    primary_tank = 2

    # Define the total length of time Beth needs to be underwater
    total_time = 8

    # Define the length of time each supplemental tank provides
    supplemental_tank = 1

    # Calculate the number of supplemental tanks needed
    supplemental_tanks_needed = (total_time - primary_tank) / supplemental_tank

    # Round up to the nearest whole number since Beth can only use whole tanks
    supplemental_tanks_needed = round(supplemental_tanks_needed + 0.5)

    result = supplemental_tanks_needed
    return result

print(solution())