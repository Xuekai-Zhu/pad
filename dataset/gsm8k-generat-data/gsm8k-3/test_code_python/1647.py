def solution():
    """Ellie and Sarah get lost in a house of mirrors and have to travel through it a few times before they finally get out. They both pass through the room with tall mirrors 3 times each and the room with wide mirrors 5 times each. Sarah sees her reflection 10 times in every tall mirror and 5 times in every wide mirror. Ellie sees her reflection 6 times in every tall mirror and 3 times in every wide mirror. How many times did they see their reflections in total?"""
    # Number of times they pass through the tall mirror rooms
    tall_mirror_trips = 3
    # Number of times they pass through the wide mirror rooms
    wide_mirror_trips = 5

    # Sarah's reflections in tall mirrors
    sarah_tall_reflections = 10 * tall_mirror_trips
    # Sarah's reflections in wide mirrors
    sarah_wide_reflections = 5 * wide_mirror_trips
    # Sarah's total reflections
    sarah_total_reflections = sarah_tall_reflections + sarah_wide_reflections

    # Ellie's reflections in tall mirrors
    ellie_tall_reflections = 6 * tall_mirror_trips
    # Ellie's reflections in wide mirrors
    ellie_wide_reflections = 3 * wide_mirror_trips
    # Ellie's total reflections
    ellie_total_reflections = ellie_tall_reflections + ellie_wide_reflections

    # Total reflections
    total_reflections = sarah_total_reflections + ellie_total_reflections

    # Display the total number of reflections
    result = total_reflections
    return result

print(solution())