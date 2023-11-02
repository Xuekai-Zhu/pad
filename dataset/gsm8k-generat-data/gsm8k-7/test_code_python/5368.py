def solution():
    num_pepperoni = 30
    num_ham = 2 * num_pepperoni
    num_sausage = num_pepperoni + 12
    num_slices = 6

    # Calculate the total number of meat pieces used for each pizza
    total_meat_pieces = num_pepperoni + num_ham + num_sausage

    # Calculate the average number of meat pieces per slice of pizza
    pieces_per_slice = total_meat_pieces / num_slices
    result = pieces_per_slice
    return result

print(solution())