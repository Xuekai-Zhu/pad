def solution():
    """Debora has 12 more dresses than Melissa. Melissa has half the number of dresses Emily has. If Emily has 16 dresses, how many dresses do the three of them have in total?"""
    # Define the number of dresses Emily has
    emily_dresses = 16

    # Calculate the number of dresses Melissa has
    melissa_dresses = emily_dresses / 2

    # Calculate the number of dresses Debora has
    debora_dresses = melissa_dresses + 12

    # Calculate the total number of dresses they have
    total_dresses = emily_dresses + melissa_dresses + debora_dresses

    # Display the total number of dresses they have
    result = total_dresses
    return result

print(solution())