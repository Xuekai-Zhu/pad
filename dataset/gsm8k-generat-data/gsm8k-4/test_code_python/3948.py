def solution():
    """John started weightlifting when he was 16. When he first started he could Clean & Jerk 80 kg and he could Snatch 50 kg. He manages to double his clean and jerk and increase his snatch by 80%. What is his new combined total lifting capacity?"""
    # Define the initial Clean & Jerk and Snatch weights
    clean_and_jerk = 80
    snatch = 50

    # Double the Clean & Jerk weight
    clean_and_jerk *= 2

    # Increase the Snatch weight by 80%
    snatch *= 1.8

    # Calculate the new total lifting capacity
    total_capacity = clean_and_jerk + snatch

    # Return the result
    result = total_capacity
    return result

print(solution())