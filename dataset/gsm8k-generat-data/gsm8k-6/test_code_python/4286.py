def solution():
    initial_blondes = 30  # number of blonde-haired girls initially
    new_blondes = 10  # number of blondes added to the choir
    total_girls = 80  # total number of girls after adding the new ones

    # Calculate the number of black-haired girls in the choir
    black_haired = total_girls - (initial_blondes + new_blondes)
    result = black_haired
    return result

print(solution())