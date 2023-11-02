def solution():
    num_students_swanson = 25
    num_zits_swanson = 5

    num_students_jones = 32
    num_zits_jones = 6

    # Calculate the total number of zits in Ms. Swanson's class
    total_zits_swanson = num_students_swanson * num_zits_swanson

    # Calculate the total number of zits in Mr. Jones' class
    total_zits_jones = num_students_jones * num_zits_jones

    # Calculate the difference in the total number of zits
    difference_zits = total_zits_jones - total_zits_swanson
    result = difference_zits
    return result

print(solution())