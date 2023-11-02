def solution():
    # Define the amount of orange punch
    orange_punch = 4.5

    # Define the amount of cherry punch, which is twice the amount of orange punch
    cherry_punch = 2 * orange_punch

    # Define the amount of apple juice, which is 1.5 liters less than cherry punch
    apple_juice = cherry_punch - 1.5

    # Calculate the total amount of fruit punch
    total_fruit_punch = orange_punch + cherry_punch + apple_juice
    result = total_fruit_punch
    return result

print(solution())