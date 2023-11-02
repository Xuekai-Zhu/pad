def solution():
    # Calculate the size of the 6th biggest doll in centimeters
    doll_size = 243  # size of the biggest doll
    for i in range(5):  # loop through the sizes of the nested dolls up to the 6th doll
        doll_size *= 2/3  # each doll is 2/3 of the size of the doll that contains it
    result = doll_size
    return result

print(solution())