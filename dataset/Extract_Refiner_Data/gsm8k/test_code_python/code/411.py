def solution():
    
    # Define the number of apples gathered from the tallest trees
    tallest_apples = 30

    # Define the number of apples gathered from the shortest trees
    shortest_apples = tallest_apples / 2

    # Define the number of apples gathered from the average trees
    average_apples = average_apples * 2

    # Calculate the total number of apples gathered
    total_apples = 500

    # Calculate the number of apples gathered by Joanne's sister
    sister_apples = tallest_apples * 2 + shortest_apples * 3

    # Calculate the total number of apples gathered by both sisters
    total_sister_apples = sister_apples + average_apples

    # Calculate the number of apples left over
    apples_left_over = total_apples - total_sister_apples

    # Display the number of apples gathered
    result = apples_left_over
    return result

print(solution())