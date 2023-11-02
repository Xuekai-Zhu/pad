def solution():
    """Bryan starts exercising at home during quarantine. To start, he decides to do 3 sets of 15 push-ups each. Near the end of the third set, he gets tired and does 5 fewer push-ups. How many push-ups did he do in total?"""
    # Define the number of push-ups in each set
    PUSHUPS_PER_SET = 15

    # Calculate the total number of push-ups before getting tired
    total_pushups = 3 * PUSHUPS_PER_SET

    # Subtract the number of push-ups he did less in the third set
    total_pushups -= 5

    # Display the total number of push-ups
    result = total_pushups
    return result

print(solution())