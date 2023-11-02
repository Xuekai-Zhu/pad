def solution():
    """Madison takes her dog to the dog park. Counting Madison's dog, half the dogs have spots and 1/5 have pointy ears. If 15 dogs have spots, how many have pointy ears?"""
    total_dogs = 2 * 15    # Since half the dogs have spots
    pointy_ear_dogs = total_dogs // 5  # 1/5 of the dogs have pointy ears
    result = pointy_ear_dogs
    return result

print(solution())