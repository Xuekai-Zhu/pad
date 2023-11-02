def solution():
    """Jerry charges $20 to pierce someone's nose and 50% more to pierce their ears. If he pierces 6 noses and 9 ears, how much money does he make?"""
    # Define the cost to pierce a nose and the additional cost to pierce ears
    nose_cost = 20
    ear_cost = nose_cost * 1.5

    # Calculate the total earnings from piercing noses and ears
    nose_earnings = nose_cost * 6
    ear_earnings = ear_cost * 9
    total_earnings = nose_earnings + ear_earnings

    # return the result
    result = total_earnings
    return result

print(solution())