def solution():
    num_peter_pictures = 8
    num_quincy_pictures = num_peter_pictures + 20
    total_pictures = 41

    # Calculate the number of pictures that Randy drew
    num_randy_pictures = total_pictures - num_peter_pictures - num_quincy_pictures
    result = num_randy_pictures
    return result

print(solution())