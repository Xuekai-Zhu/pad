def solution():
    """The length of the straight part of a river is three times shorter than the crooked part. If the river is 80 miles long, how long is the straight part of the river?"""
    total_length = 80
    crooked_length = total_length / 4
    straight_length = total_length - crooked_length
    result = straight_length
    return result

print(solution())