def solution():
    # Calculate total number of children and total class sizes
    total_children = 13 + 20 + 15 + 22
    class1_size = 13 + 20
    class2_size = 15 + 22

    # Calculate average class sizes
    avg_class1_size = class1_size / 2
    avg_class2_size = class2_size / 2
    overall_avg = total_children / 2

    # Calculate the final average class size
    final_avg = (avg_class1_size + avg_class2_size + overall_avg) / 3
    result = final_avg
    return result

print(solution())