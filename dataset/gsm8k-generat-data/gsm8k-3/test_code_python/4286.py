def solution():
    """Lizzy's school choir has a mixture of 80 blonde and black-haired girls. Their teacher decides to add 10 more girls to the choir, who turn out to be blonde. If there were 30 blonde-haired girls in the choir initially, how many black-haired girls are present?"""
    # Define the initial number of blonde-haired girls and total number of girls
    initial_blondes = 30
    total_girls = 80

    # Calculate the initial number of black-haired girls
    initial_blacks = total_girls - initial_blondes

    # Add 10 blonde-haired girls to the choir
    final_blondes = initial_blondes + 10

    # Calculate the final number of black-haired girls
    final_blacks = total_girls - final_blondes

    # Display the final number of black-haired girls
    result = final_blacks
    return result

print(solution())