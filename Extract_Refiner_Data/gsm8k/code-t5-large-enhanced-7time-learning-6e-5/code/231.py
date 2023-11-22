def solution():
    
    # Define the number of friends and slices per friend
    num_friends = 20
    slices_per_friend = 4

    # Calculate the total number of slices
    total_slices = num_friends * slices_per_friend

    # Calculate the number of pizzas needed
    pizzas_needed = total_slices // 8

    # return the result
    result = pizzas_needed
    return result

print(solution())