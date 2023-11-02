def solution():
    """Evan’s dog weighs 63 pounds; it weighs 7 times as much as Ivan’s dog. Together, what is the weight of the dogs?"""
    evan_dog_weight = 63
    ivan_dog_weight = evan_dog_weight / 7
    total_dog_weight = evan_dog_weight + ivan_dog_weight
    result = total_dog_weight
    return result

print(solution())