def solution():
    group1 = 9
    group2 = 10
    group3 = 11
    tissues_per_box = 40
    total_tissues1 = group1 * tissues_per_box
    total_tissues2 = group2 * tissues_per_box
    total_tissues3 = group3 * tissues_per_box
    total_tissues = total_tissues1 + total_tissues2 + total_tissues3
    result = total_tissues
    return result

print(solution())