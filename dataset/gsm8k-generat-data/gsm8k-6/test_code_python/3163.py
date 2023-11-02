def solution():
    # Calculate the number of slices of cheese and onion needed for the class
    total_cheese = 6 * 18 - 8  # 6 pizzas with 18 slices each, minus 8 leftover cheese pieces
    total_onion = 6 * 18 - 4   # 6 pizzas with 18 slices each, minus 4 leftover onion pieces
    
    # Calculate the number of students in the class
    # Each student eats 2 pieces of cheese and 1 piece of onion, so we need to find the common multiple of 2 and 1
    # that is closest to the total number of cheese and onion slices needed
    total_slices = total_cheese + total_onion
    for i in range(1, total_slices+1):
        if i % 2 == 0 and (total_slices-i) % 1 == 0:
            num_students = i//2
            break
    
    result = num_students
    return result

print(solution())