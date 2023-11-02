def solution():
    """A roll of 25 m wire weighs 5 kg. How much does a 75 m roll weigh?"""
    length_1 = 25
    weight_1 = 5
    length_2 = 75
    weight_2 = weight_1 * (length_2/length_1)
    result = weight_2
    return result

print(solution())