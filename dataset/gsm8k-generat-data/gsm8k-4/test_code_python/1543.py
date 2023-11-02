def solution():
    """Ken can do 20 sit-ups without stopping. Nathan can do twice as many, and Bob can do half the number of Ken and Nathan's combined sit-ups. How many more sit-ups can Bob do compared to Ken?"""
    # Define the number of sit-ups Ken can do
    ken_situps = 20

    # Define the number of sit-ups Nathan can do
    nathan_situps = ken_situps * 2

    # Define the number of sit-ups Bob can do
    bob_situps = (ken_situps + nathan_situps) / 2

    # Calculate the difference in sit-ups between Bob and Ken
    situp_difference = bob_situps - ken_situps

    # return the result
    result = situp_difference
    return result

print(solution())