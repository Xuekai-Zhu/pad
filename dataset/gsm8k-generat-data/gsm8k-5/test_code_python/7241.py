def solution():
    total_flowers = 400
    tulips = 120
    roses = total_flowers - tulips
    white_roses = 80
    red_roses = roses - white_roses
    value_red_roses = 0.75

    # Calculate the earnings from selling half of the red roses
    earnings = (red_roses / 2) * value_red_roses
    result = earnings
    return result

print(solution())