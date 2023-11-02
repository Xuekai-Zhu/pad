def solution():
    """Sandra had 2 different bags of candy. Each of her bags had 6 pieces of candy left. Her brother, Roger, also had 2 bags of candy. One of his bags of candy had 11 pieces left and the other had 3 pieces left. How much more candy did Roger have?"""
    sandra_total_candy = 2 * 6
    roger_total_candy = 11 + 3
    difference = roger_total_candy - sandra_total_candy
    result = difference
    return result

print(solution())