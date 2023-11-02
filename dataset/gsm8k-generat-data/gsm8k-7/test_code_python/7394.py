def solution():
    num_northern_tents = 100
    num_east_tents = num_northern_tents * 2
    num_center_tents = num_northern_tents * 4
    num_southern_tents = 200

    # Calculate the total number of tents
    total_tents = num_northern_tents + num_east_tents + num_center_tents + num_southern_tents
    result = total_tents
    return result

print(solution())