def solution():
    orange_punch = 4.5  # liters of orange punch
    cherry_punch = 2 * orange_punch  # twice the amount of orange punch
    apple_juice = cherry_punch - 1.5  # 1.5 liters less than cherry punch

    # Calculate the total liters of fruit punch
    total_punch = orange_punch + cherry_punch + apple_juice
    result = total_punch
    return result

print(solution())