def solution():
    # Calculate the amount of oil in the initial tank that was poured into the larger tank
    initial_oil = 4000
    oil_poured = 0.75 * initial_oil

    # Calculate the current amount of oil in the larger tank
    current_oil = oil_poured + 3000

    # Calculate the amount of oil needed to make the larger tank half-full
    half_full = 0.5 * 20000
    oil_needed = half_full - current_oil
    result = oil_needed
    return result

print(solution())