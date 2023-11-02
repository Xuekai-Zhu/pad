def solution():
    # Calculate the number of people in the stadium when it was 3/4 full
    num_people = 2000 * (3/4)  

    # Calculate the total fees collected when the stadium was 3/4 full
    total_fees_3_4_full = num_people * 20  

    # Calculate the total fees collected when the stadium is full
    total_fees_full = 2000 * 20  

    # Calculate the difference in fees collected
    difference = total_fees_full - total_fees_3_4_full  
    result = difference
    return result

print(solution())