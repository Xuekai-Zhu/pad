def solution():
    """Bryan starts exercising at home during quarantine. To start, he decides to do 3 sets of 15 push-ups each. Near the end of the third set, he gets tired and does 5 fewer push-ups. How many push-ups did he do in total?"""
    # Define the number of push-ups in each set
    push_ups_per_set = 15

    # Define the number of sets
    sets = 3

    # Calculate the total number of push-ups originally planned
    total_push_ups = push_ups_per_set * sets

    # Calculate the number of push-ups he did in the last set
    final_push_ups = push_ups_per_set - 5

    # Calculate the total number of push-ups he did
    total_push_ups_done = (sets - 1) * push_ups_per_set + final_push_ups

    # Display the result
    result = total_push_ups_done
    return result

print(solution())