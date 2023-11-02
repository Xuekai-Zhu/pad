def solution():
    """Quinton brought 40 cupcakes to school on his birthday. He gave a cupcake to each of the 18 students in Ms. Delmont's class. He also gave a cupcake to each of the 16 students in Mrs. Donnelly's class. He also gave a cupcake to Ms. Delmont, Mrs. Donnelly, the school nurse, and the school principal. How many cupcakes did he have left over?"""
    # Define the number of cupcakes brought to school
    cupcakes = 40

    # Define the number of cupcakes given away
    given_away = 18 + 16 + 4

    # Calculate the number of cupcakes left over
    left_over = cupcakes - given_away

    # Display the number of cupcakes left over
    result = left_over
    return result

print(solution())