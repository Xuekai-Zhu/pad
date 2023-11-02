def solution():
    """Lizzy's school choir has a mixture of 80 blonde and black-haired girls. Their teacher decides to add 10 more girls to the choir, who turns out to be blonde. If there were 30 blonde-haired girls in the choir initially, how many black-haired girls are present?"""
    # Define the initial number of blonde-haired girls and the total number of girls
    initial_blonde = 30
    total_girls = 80

    # Calculate the initial number of black-haired girls
    initial_black = total_girls - initial_blonde

    # Add the 10 new blonde-haired girls
    new_blonde = 10
    final_blonde = initial_blonde + new_blonde

    # Calculate the final number of black-haired girls
    final_black = total_girls - final_blonde

    # Return the result
    result = final_black
    return result

print(solution())