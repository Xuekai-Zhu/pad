def solution():
    # Calculate the total number of eggs the family has now
    remaining_eggs = 10 - 5  # the mother used 5 eggs to make an omelet
    new_eggs = 2 * 3  # 2 chickens laid 3 eggs each
    total_eggs = remaining_eggs + new_eggs
    result = total_eggs
    return result

print(solution())