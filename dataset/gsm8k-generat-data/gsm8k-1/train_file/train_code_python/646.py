def solution():
    """Quinton brought 40 cupcakes to school on his birthday. He gave a cupcake to each of the 18 students in Ms. Delmont's class. He also gave a cupcake to each of the 16 students in Mrs. Donnelly's class. He also gave a cupcake to Ms. Delmont, Mrs. Donnelly, the school nurse, and the school principal. How many cupcakes did he have left over?"""
    total_cupcakes = 40
    cupcakes_given = 18 + 16 + 4  # 2 teachers, nurse, principal
    cupcakes_left = total_cupcakes - cupcakes_given
    result = cupcakes_left
    return result

print(solution())