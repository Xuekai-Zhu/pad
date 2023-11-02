def solution():
    
    initial_pairs = 4
    week1_pairs = 12
    week2_pairs = week1_pairs + 4
    week3_pairs = (week1_pairs + week2_pairs) / 2
    week4_pairs = week3_pairs - 3
    total_pairs = initial_pairs + week1_pairs + week2_pairs + week3_pairs + week4_pairs
    result = total_pairs
    return result

print(solution())