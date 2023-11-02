def solution():
    orange_punch = 4.5  # liters of orange punch
    cherry_punch = 2 * orange_punch  # liters of cherry punch (twice as much as orange punch)
    apple_juice = cherry_punch - 1.5  # liters of apple juice (1.5 liters less than cherry punch)
    fruit_punch = orange_punch + cherry_punch + apple_juice  # total liters of fruit punch

    result = fruit_punch
    return result

print(solution())