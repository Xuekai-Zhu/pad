def solution():
    """Roland needs a length of thread to complete an exercise. He has a 12cm long thread but his teacher says he needs an additional three-quarters of what he has. What is the total length required?"""
    # Define the initial thread length and the additional thread required
    initial_length = 12
    additional_length_ratio = 3/4

    # Calculate the additional thread required
    additional_length = additional_length_ratio * initial_length

    # Calculate the total length required
    total_length = initial_length + additional_length

    # return the result
    result = total_length
    return result

print(solution())