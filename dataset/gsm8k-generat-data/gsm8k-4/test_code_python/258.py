def solution():
    """Anne is 2 times as tall as her sister while Bella is 3 times as tall as Anne. If Anne is 80cm tall, what is the height difference between Bella and Anne's sister?"""
    # Define Anne's height
    anne_height = 80

    # Calculate Anne's sister's height
    sister_height = anne_height / 2

    # Calculate Bella's height
    bella_height = anne_height * 3

    # Calculate the height difference between Bella and Anne's sister
    height_diff = bella_height - sister_height

    result = height_diff
    return result

print(solution())