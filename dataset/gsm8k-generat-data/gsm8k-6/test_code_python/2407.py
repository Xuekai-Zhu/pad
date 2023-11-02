def solution():
    # Calculate the number of treats that Jane brought
    treats_jane = (4/3) * (90/3)  # Jane brings 75% as many pieces of bread as treats, and Wanda brings 3 times as many pieces of bread as treats
    # Calculate the number of pieces of bread that Jane brought
    bread_jane = 90/3  # Wanda brings 3 times as many pieces of bread as treats, and Wanda brought 90 pieces of bread
    # Calculate the number of treats that Wanda brought
    treats_wanda = (1/2) * treats_jane  # Wanda brings half as many treats as Jane
    # Calculate the total number of pieces of bread and treats that Wanda and Jane brought
    total_pieces = treats_jane + bread_jane + treats_wanda + 90  # Wanda brought 90 pieces of bread
    result = total_pieces
    return result

print(solution())