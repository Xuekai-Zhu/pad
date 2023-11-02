def solution():
    length_of_largest = 45
    width_of_largest = 30
    length_of_smallest = 15
    width_of_smallest = 8
    
    largest_area = length_of_largest * width_of_largest
    smallest_area = length_of_smallest * width_of_smallest
    difference = largest_area - smallest_area
    
    result = difference
    
    return result

print(solution())