def solution():
    total_fruit = 12
    chosen_apples = 3
    chosen_bananas = 4

    # Calculate the number of oranges needed to reach 12 total pieces of fruit
    oranges_needed = total_fruit - chosen_apples - chosen_bananas
    result = oranges_needed
    return result

print(solution())