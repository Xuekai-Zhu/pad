def solution():
    """Quinton brought 40 cupcakes to school on his birthday. He gave a cupcake to each of the 18 students in Ms. Delmont's class. He also gave a cupcake to each of the 16 students in Mrs. Donnelly's class. He also gave a cupcake to Ms. Delmont, Mrs. Donnelly, the school nurse, and the school principal. How many cupcakes did he have left over?"""
    # Define the initial number of cupcakes
    cupcakes = 40

    # Subtract the cupcakes given to Ms. Delmont's class
    cupcakes -= 18

    # Subtract the cupcakes given to Mrs. Donnelly's class
    cupcakes -= 16

    # Subtract the cupcakes given to the four individuals
    cupcakes -= 4

    # return the result
    result = cupcakes
    return result

print(solution())