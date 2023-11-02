def solution():
    emily_dresses = 16  # Emily has 16 dresses
    melissa_dresses = emily_dresses / 2  # Melissa has half the number of dresses Emily has
    debora_dresses = melissa_dresses + 12  # Debora has 12 more dresses than Melissa

    # Calculate the total number of dresses
    total_dresses = emily_dresses + melissa_dresses + debora_dresses
    result = total_dresses
    return result

print(solution())