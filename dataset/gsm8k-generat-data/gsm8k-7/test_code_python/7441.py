def solution():
    num_randy_pics = 5
    num_peter_pics = num_randy_pics + 3
    num_quincy_pics = num_peter_pics + 20

    # Calculate the total number of pictures drawn
    total_pics = num_randy_pics + num_peter_pics + num_quincy_pics
    result = total_pics
    return result

print(solution())