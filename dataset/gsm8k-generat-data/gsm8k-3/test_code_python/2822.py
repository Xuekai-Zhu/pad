def solution():
    """Jennifer will be 30 years old in ten years. At that time, her sister Jordana will be three times as old Jennifer. How old is Jennifer's sister now?"""
    # Define Jennifer's age in ten years
    jennifer_future_age = 30

    # Calculate Jennifer's current age
    jennifer_age = jennifer_future_age - 10

    # Calculate Jordana's age in ten years
    jordana_future_age = jennifer_future_age * 3

    # Calculate Jordana's current age
    jordana_age = jordana_future_age - 10

    # Display Jordana's current age
    result = jordana_age
    return result

print(solution())