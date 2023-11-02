def solution():
    ammonia_smell = "pungent"
    dog_sense_of_smell = 40
    if dog_sense_of_smell > 1 and ammonia_smell == "pungent":
        result = "yes"
    else:
        result = "no"
    return result

print(solution())