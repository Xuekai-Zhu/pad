def solution():
    """Elijah has one dog that is one-fourth the weight of Kory’s dog and another dog that is half the weight of Kory’s dog. If Kory’s dog is 60 pounds, how much do Elijah and Kory’s dogs weigh altogether, in pounds?"""
    kory_weight = 60
    elijah_dog1_weight = kory_weight / 4
    elijah_dog2_weight = kory_weight / 2
    total_weight = kory_weight + elijah_dog1_weight + elijah_dog2_weight
    result = total_weight
    return result

print(solution())