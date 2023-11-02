def solution():
    total_fruit = 10  # Mark had 10 pieces of fruit for the week
    remaining_fruit = total_fruit - 2  # Mark kept 2 pieces of fruit for next week
    fruit_brought_to_school = 3  # Mark brought 3 pieces of fruit to school on Friday

    # Calculate the number of fruit Mark ate in the first four days of the week
    fruit_eaten = remaining_fruit - fruit_brought_to_school
    result = fruit_eaten
    return result

print(solution())