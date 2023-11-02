def solution():
    # Calculate the cost in cents of replacing the dress
    dress_cost = 35 * 100  

    # Calculate the total value in cents of the quarters
    quarters_value = 160 * 25  

    # Calculate the remaining value in cents of the quarters after paying for the dress
    remaining_value = quarters_value - dress_cost  

    # Calculate the number of quarters remaining
    quarters_remaining = remaining_value / 25  
    result = quarters_remaining
    return result

print(solution())