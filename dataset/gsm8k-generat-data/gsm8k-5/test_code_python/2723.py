def solution():
    total_length = 80  # The river is 80 miles long
    crooked_part = total_length / 4  # The crooked part is four times longer than the straight part
    straight_part = total_length - crooked_part  # The straight part is the remaining length

    result = straight_part
    return result

print(solution())