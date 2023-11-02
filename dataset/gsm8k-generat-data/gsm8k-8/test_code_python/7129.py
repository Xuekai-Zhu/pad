def solution():
    # Define the number of books borrowed and returned
    borrowed_initially = 5
    returned_first_time = 3
    borrowed_second_time = 5
    returned_second_time = 2
    borrowed_third_time = 7

    # Calculate the net number of books borrowed
    net_borrowed = borrowed_initially - returned_first_time + borrowed_second_time - returned_second_time + borrowed_third_time

    result = net_borrowed
    return result

print(solution())