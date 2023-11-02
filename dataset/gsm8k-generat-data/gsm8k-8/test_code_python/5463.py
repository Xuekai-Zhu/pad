def solution():
    # Calculate the number of students who collected 12 cans
    num_12_cans = (30 // 2)

    # Calculate the number of students who collected 4 cans
    num_4_cans = 13

    # Calculate the total number of cans collected by those who collected 12 cans
    total_12_cans = num_12_cans * 12

    # Calculate the total number of cans collected by those who collected 4 cans
    total_4_cans = num_4_cans * 4

    # Calculate the total number of cans collected by the class
    total_cans = total_12_cans + total_4_cans

    result = total_cans
    return result

print(solution())