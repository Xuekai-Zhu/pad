def solution():
    # Calculate the total number of apples in the group
    total_apples = 20 + 60 + 40
 
    # Calculate the average number of apples per person in the group
    average_apples = total_apples / 3
 
    # Calculate the number of times Jim's number of apples can fit into the average amount
    times_fit = average_apples // 20
 
    result = times_fit
    return result

print(solution())