def solution():
    movie1_length = 2
    movie2_length = movie1_length * 1.5
    movie3_length = movie1_length + movie2_length - 1
    total_length = movie1_length + movie2_length + movie3_length
    result = total_length
    return result

print(solution())