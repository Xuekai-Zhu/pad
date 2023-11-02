def solution():
    """Elise is learning to write and decides to keep re-writing the alphabet until she knows it. She writes it in full twice, writes half of it once, then re-writes everything she has already written. How many letters has Elise written in total?"""
    alphabet_length = 26
    half_alphabet_length = alphabet_length/2
    total_letters = (alphabet_length*2) + half_alphabet_length + (alphabet_length*3)
    result = total_letters
    return result

print(solution())