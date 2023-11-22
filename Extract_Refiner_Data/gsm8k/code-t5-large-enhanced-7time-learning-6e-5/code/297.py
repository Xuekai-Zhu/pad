def solution():
    
    # Define the number of pages printed on each side of the paper
    left_back = 1
    left_front = 2
    right_back = 32
    right_front = 31

    # Calculate the total number of pieces of paper used in a 32-page tabloid
    total_paper = left_back + left_front + right_back + right_front

    # Display the total number of pieces of paper used
    result = total_paper
    return result

print(solution())