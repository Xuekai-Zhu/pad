def solution():
    total_flowers = 400
    num_tulips = 120

    # Calculate the number of roses
    num_roses = total_flowers - num_tulips

    # Calculate the number of white roses
    num_white_roses = 80

    # Calculate the number of red roses
    num_red_roses = num_roses - num_white_roses

    # Calculate the earnings if she sells half of the red roses
    half_red_roses = num_red_roses / 2
    earnings = half_red_roses * 0.75
    result = earnings
    return result

print(solution())