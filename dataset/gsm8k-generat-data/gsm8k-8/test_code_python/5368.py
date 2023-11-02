def solution():
    # Define the number of pieces of pepperoni, ham, and sausage
    pepperoni = 30
    ham = 2 * pepperoni
    sausage = pepperoni + 12

    # Calculate the total number of pieces of meat
    total_meat = pepperoni + ham + sausage

    # Calculate the number of pieces of meat per slice
    pieces_per_slice = total_meat / 6
    result = pieces_per_slice
    return result

print(solution())