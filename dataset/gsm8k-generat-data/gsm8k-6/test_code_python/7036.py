def solution():
    # Find the number of dresses Melissa has
    melissa_dresses = (1/2) * 16  # Emily has 16 dresses and Melissa has half of that

    # Find the number of dresses Debora has
    debora_dresses = melissa_dresses + 12  # Debora has 12 more dresses than Melissa

    # Find the total number of dresses the three of them have
    total_dresses = melissa_dresses + debora_dresses + 16  # Emily has 16 dresses
    result = total_dresses
    return result

print(solution())