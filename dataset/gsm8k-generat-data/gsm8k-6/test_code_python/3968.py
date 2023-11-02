def solution():
    # Let b be the number of brown eggs and w be the number of white eggs
    # We know that w = 3b
    
    # After dropping the basket, Linda is left with 5 brown eggs and a total of 12 eggs
    # So 5 + w = 12
    # Substituting w = 3b, we get 5 + 3b = 12
    
    b = 2  # Solve for b: b = (12 - 5) / 3
    w = 6  # Therefore w = 3 * b
    
    # Linda started with a total of b + w eggs
    starting_eggs = b + w
    
    # After the accident, she had 12 eggs left, so she broke starting_eggs - 12 eggs
    broken_eggs = starting_eggs - 12
    
    result = broken_eggs
    return result

print(solution())