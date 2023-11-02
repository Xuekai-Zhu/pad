def solution():
    raw_carrot_release = 0.03
    improved_release = 0.39

    # Calculate the amount of retinal released from raw carrots and improved method
    raw_carrot_retinal = raw_carrot_release * 100
    improved_retinal = improved_release * 100

    if raw_carrot_retinal > improved_retinal:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())