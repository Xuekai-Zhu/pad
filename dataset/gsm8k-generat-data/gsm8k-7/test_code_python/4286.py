def solution():
    initial_blondes = 30
    total_girls = 80
    new_blondes = 10

    # Calculate the initial number of black-haired girls
    initial_black = total_girls - initial_blondes

    # Add the new blondes to the total number of blondes
    total_blondes = initial_blondes + new_blondes

    # Calculate the new total number of black-haired girls
    new_total_black = total_girls - total_blondes

    # Calculate the number of black-haired girls present initially
    black_initial = initial_black

    # Calculate the number of black-haired girls present after the new girls are added
    black_new = new_total_black

    # Return the number of black-haired girls present after the new girls are added
    result = black_new
    return result

print(solution())