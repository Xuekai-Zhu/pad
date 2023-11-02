def solution():
    """The region east of plain A is 50 square miles less than the region east of plain B. If plain B has 200 square miles, how many square miles do the plains have in total?"""
    plain_b_size = 200
    plain_a_size = plain_b_size - 50
    total_size = plain_a_size + plain_b_size
    result = total_size
    return result

print(solution())