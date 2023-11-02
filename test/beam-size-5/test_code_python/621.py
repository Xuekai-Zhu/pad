def solution():
    
    # Define the number of rows and flowers per row
    rows = 10
    flowers_per_row = 20

    # Calculate the total number of flowers in the garden
    total_flowers = rows * flowers_per_row

    # Calculate the number of flowers that have bloomed
    bloomed_flowers = total_flowers * (4/5)

    # Display the number of flowers that have bloomed
    result = bloomed_flowers
    return result

print(solution())