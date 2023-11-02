def solution():
    # Define the length of Johnny's essay
    johnny_length = 150

    # Define the length of Madeline's essay
    madeline_length = johnny_length * 2

    # Define the length of Timothy's essay
    timothy_length = madeline_length + 30

    # Calculate the total length of all three essays
    total_length = johnny_length + madeline_length + timothy_length

    # Calculate the number of pages needed to write all three essays
    num_pages = total_length / 260
    result = num_pages
    return result

print(solution())