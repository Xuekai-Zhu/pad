def solution():
    # Define the initial number of blonde-haired girls
    initial_blondes = 30

    # Calculate the initial number of black-haired girls
    initial_blacks = 80 - initial_blondes

    # Add 10 blonde-haired girls to the choir
    final_blondes = initial_blondes + 10

    # Calculate the final number of black-haired girls
    final_blacks = 80 - final_blondes

    result = final_blacks
    return result

print(solution())