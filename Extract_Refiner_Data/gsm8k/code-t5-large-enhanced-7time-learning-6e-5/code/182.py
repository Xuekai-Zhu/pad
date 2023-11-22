def solution():
    
    # Define the number of pieces of straw distributed among the rodents
    straw_distributed = 160

    # Calculate the number of pieces of straw distributed among the rodents
    straw_distributed_rats = 3 * 6
    straw_distributed_hamsters = 10 * 5
    straw_distributed_rabbits = 20

    # Calculate the total number of pieces of straw distributed among the rodents
    total_straw_distributed = straw_distributed_rats + straw_distributed_hamsters + straw_distributed_rabbits

    # Calculate the number of rats that can be made with the straw
    num_rats = total_straw_distributed // 6

    # Display the number of rats
    result = num_rats
    return result

print(solution())