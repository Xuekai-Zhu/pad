def solution():
    # Define the number of rows and flowers per row
    num_rows = 50
    flowers_per_row = 400

    # Calculate the total number of flowers
    total_flowers = num_rows * flowers_per_row

    # Calculate the number of flowers cut
    flowers_cut = 0.6 * total_flowers

    # Calculate the number of flowers remaining
    flowers_remaining = total_flowers - flowers_cut
    result = flowers_remaining
    return result

print(solution())