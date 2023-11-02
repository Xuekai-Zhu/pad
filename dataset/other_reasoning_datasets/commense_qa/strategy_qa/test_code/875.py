def solution():
    disorders_that_can_be_masked = ["Depression", "Anxiety", "Bipolar Disorder"]
    # Check if there are any disorders that can be masked
    if disorders_that_can_be_masked:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())