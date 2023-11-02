def solution():
    # Calculate the total distance Carrie drove over the four days
    total_distance = 135 + 135 + 124 + 159 + 189  # the sum of distance traveled each day
    # Calculate the number of times Carrie charged her phone
    num_charges = total_distance // 106  # integer division to get the number of times Carrie charged her phone 
    result = num_charges
    return result

print(solution())