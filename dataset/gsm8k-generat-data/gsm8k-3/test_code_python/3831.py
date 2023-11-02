def solution():
    """Jerry bought 48 firecrackers for the 4th of July. A police officer discovered and confiscated 12 of them. 1/6 of the remaining ones were defective. If Jerry set off half the good firecrackers, how many firecrackers did he set off?"""
    # Define the number of firecrackers originally bought
    original_count = 48

    # Subtract the confiscated firecrackers
    remaining_count = original_count - 12

    # Calculate the number of defective firecrackers
    defective_count = remaining_count // 6

    # Calculate the number of good firecrackers
    good_count = remaining_count - defective_count

    # Calculate the number of firecrackers set off
    set_off_count = good_count // 2

    # Display the number of firecrackers set off
    result = set_off_count
    return result

print(solution())