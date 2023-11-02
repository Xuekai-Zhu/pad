def solution():
    total_fruit = 12  # Mark wants to buy a total of 12 pieces of fruit
    apples_chosen = 3  # Mark has already chosen 3 apples
    bananas_chosen = 4  # Mark has a bunch of bananas containing 4 bananas
    oranges_needed = total_fruit - apples_chosen - bananas_chosen  # Mark needs to pick out this many oranges to have 12 total pieces of fruit
    result = oranges_needed
    return result

print(solution())