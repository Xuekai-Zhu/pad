def solution():
    initial_thickness = 3
    num_foldings = 4

    # Calculate the final thickness by doubling the thickness for each folding
    final_thickness = initial_thickness * (2 ** num_foldings)
    result = final_thickness
    return result

print(solution())