def solution():
    # Define the temperature range of magma and the melting point of polycarbonate plastic
    magma_temp_range = range(1300, 2401)
    plastic_melt_temp = 311
    # Check if the melting point of polycarbonate plastic is lower than the minimum temperature of magma
    if plastic_melt_temp < min(magma_temp_range):
        result = "no"
    else:
        result = "yes"
    return result

print(solution())