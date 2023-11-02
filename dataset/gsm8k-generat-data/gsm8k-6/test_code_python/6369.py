def solution():
    # Calculate the length of each cut piece
    cut_length = 200/4  # divide the length of the rope by four

    # Calculate the number of pieces Stefan has left after giving half to his mother
    remaining_pieces = 4/2  # Stefan gave half of the cut pieces to his mother, so he has half left

    # Calculate the length of each piece after the remaining pieces are subdivided into two equal parts
    final_length = cut_length/2  # the remaining pieces are divided into two equal parts

    result = final_length
    return result

print(solution())