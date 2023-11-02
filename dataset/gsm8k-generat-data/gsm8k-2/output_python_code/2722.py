def solution():
    """The length of the straight part of a river is three times shorter than the crooked part. If the river is 80 miles long, how long is the straight part of the river?"""
    total_length = 80
    crooked_part = total_length / 4
    straight_part = total_length - crooked_part
    result = straight_part
    return result

print(solution())