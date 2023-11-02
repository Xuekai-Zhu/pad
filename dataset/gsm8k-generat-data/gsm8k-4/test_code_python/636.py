def solution():
    """Tina is working on her homework when she realizes she's having a hard time typing out her answers on her laptop because a lot of the keys are sticky. She is trying to get her homework done before dinner, though, so she needs to decide if she has time to clean her keyboard first. Tina knows her assignment will only take 10 minutes to complete. Dinner will be ready at 5:30 p.m. Tina decides to time how long it takes to remove and clean one key and will then multiply that time by how many keys she needs to fix. She counts 15 keys that are sticky and times it to take 3 minutes to clean one. After Tina has cleaned one key, there are 14 left to clean. How many minutes total will it take for Tina to both clean the remaining keys and finish her assignment?"""
    # Calculate the time it takes to clean one key
    time_per_key = 3

    # Calculate the time it takes to clean all the remaining keys
    remaining_keys = 14
    time_remaining = remaining_keys * time_per_key

    # Calculate the time it takes to complete the assignment
    time_assignment = 10

    # Calculate the total time needed
    total_time = time_remaining + time_assignment

    result = total_time
    return result

print(solution())