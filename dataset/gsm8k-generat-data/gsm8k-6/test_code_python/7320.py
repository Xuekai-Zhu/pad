def solution():
    # Calculate the total number of gumballs
    total_gumballs = 20 + 3*20  # Pedro has that many gumballs plus an additional number of gumballs equal to three times the number Alicia has

    # Calculate the number of gumballs Pedro takes out to eat
    gumballs_eaten = 0.4 * total_gumballs

    # Calculate the number of gumballs remaining in the bowl
    remaining_gumballs = total_gumballs - gumballs_eaten
    result = remaining_gumballs
    return result

print(solution())