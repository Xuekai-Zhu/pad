def solution():
    """Anne is 2 times as tall as her sister while Bella is 3 times as tall as Anne. If Anne is 80cm tall, what is the height difference between Bella and Anne's sister?"""
    # Define the height of Anne and her sister
    anne_height = 80
    sister_height = anne_height / 2

    # Calculate the height of Bella
    bella_height = anne_height * 3

    # Calculate the height difference between Bella and Anne's sister
    height_diff = bella_height - sister_height

    # Display the height difference
    result = height_diff
    return result

print(solution())