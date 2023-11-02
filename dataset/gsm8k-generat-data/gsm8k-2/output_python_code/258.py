def solution():
    """Anne is 2 times as tall as her sister while Bella is 3 times as tall as Anne. If Anne is 80cm tall, what is the height difference between Bella and Anne's sister?"""
    anne_height = 80
    sister_height = anne_height / 2
    bella_height = 3 * anne_height
    height_difference = bella_height - sister_height
    result = height_difference
    return result

print(solution())