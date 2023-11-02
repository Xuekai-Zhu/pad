def solution():
    """Ken can do 20 sit-ups without stopping. Nathan can do twice as many, and Bob can do half the number of Ken and Nathan's combined sit-ups. How many more sit-ups can Bob do compared to Ken?"""
    # Define the number of sit-ups each person can do
    KEN_SITUPS = 20
    NATHAN_SITUPS = 2 * KEN_SITUPS
    BOB_SITUPS = (KEN_SITUPS + NATHAN_SITUPS) / 2

    # Calculate the difference between Bob and Ken's sit-ups
    difference = BOB_SITUPS - KEN_SITUPS

    # Display the difference
    result = difference
    return result

print(solution())