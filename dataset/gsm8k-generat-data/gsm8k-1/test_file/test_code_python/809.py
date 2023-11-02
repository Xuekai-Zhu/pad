def solution():
    """John and DeSean bought a bag of marshmallows to make s'mores together. The bag has 35 marshmallows. Each S'more uses one marshmallow. If John makes 9 S'mores, DeSean makes 9 S'mores, and they dropped 3 marshmallows on the ground, how many S'mores can each kid have with the marshmallows left in the bag?"""
    marshmallows = 35
    smores_per_person = (marshmallows - 3) // 18
    result = smores_per_person
    return result

print(solution())