def solution():
    """Beth is a scuba diver. She is excavating a sunken ship off the coast of a small Caribbean island and she must remain underwater for long periods. Her primary tank, which she wears when she first enters the water, has enough oxygen to allow her to stay underwater for 2 hours. She also has several 1-hour supplemental tanks that she takes with her as well as stores on the ocean floor so she can change tanks underwater without having to come up to the surface. She will need to be underwater for 8 hours. How many supplemental tanks will she need?"""
    primary_tank = 2
    supplemental_tanks = 1
    total_hours = 8
    remaining_hours = total_hours - primary_tank
    supplemental_tanks += remaining_hours
    result = supplemental_tanks - 1
    return result

print(solution())