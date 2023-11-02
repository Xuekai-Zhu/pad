def solution():
    """One of Robi's new year's resolutions is to start saving. He started to save $2 in January. This is followed by $4 in February and $8 in March. If he continues this saving pattern, how much will be his total savings after 6 months?"""
    # Define the initial saving amount and the saving pattern
    initial_saving = 2
    saving_pattern = [2**n for n in range(6)]

    # Calculate the total savings after 6 months
    total_saving = sum(saving_pattern)

    # return the result
    result = total_saving
    return result

print(solution())