def solution():
    
    # Define the total length of fence
    total_length = 100

    # Calculate the length of fence each person gets
    sam_length = (total_length - 60) / 2
    harry_length = sam_length + 60

    # Calculate the amount left over for Sam
    leftover_fence = total_length - (sam_length + harry_length)

    # Display the amount left over for Sam
    result = leftover_fence
    return result

print(solution())