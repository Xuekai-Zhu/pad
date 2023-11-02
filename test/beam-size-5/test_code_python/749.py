def solution():
    
    # Define the initial number of glasses and plates
    initial_glasses = 8 * 12
    initial_plates = 4 * 12

    # Subtract the number of broken glasses and plates from the initial number of glasses and plates
    final_glasses = initial_glasses - 10
    final_plates = initial_plates - 6

    # Display the final number of glasses and plates
    result = final_glasses
    return result

print(solution())