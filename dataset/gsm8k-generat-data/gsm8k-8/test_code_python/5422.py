def solution():
    # Define the sum of the three consecutive integers
    total_sum = 18

    # Divide the sum by 3 to find the middle number
    middle_number = total_sum // 3

    # Use the middle number to find the smallest and largest numbers
    smallest_number = middle_number - 1
    largest_number = middle_number + 1

    result = largest_number
    return result

print(solution())