def solution():
    num_fruits_C = 9
    num_fruits_B = num_fruits_C + 3
    num_fruits_A = num_fruits_B + 4

    # Calculate the total number of fruits in all three buckets
    total_num_fruits = num_fruits_A + num_fruits_B + num_fruits_C
    result = total_num_fruits
    return result

print(solution())