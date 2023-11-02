def solution():
    giraffe_height_range = [4.3, 5.7]
    javier_sotomayor_jump_height = 2.45
    # Taking the upper limit of giraffe height range as the height of an average giraffe
    average_giraffe_height = (giraffe_height_range[0] + giraffe_height_range[1]) / 2
    if javier_sotomayor_jump_height > average_giraffe_height:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())