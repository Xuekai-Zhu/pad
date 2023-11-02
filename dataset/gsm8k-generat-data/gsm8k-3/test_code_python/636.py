def solution():
    """Tina is working on her homework when she realizes she's having a hard time typing out her answers on her laptop because a lot of the keys are sticky. She is trying to get her homework done before dinner, though, so she needs to decide if she has time to clean her keyboard first. Tina knows her assignment will only take 10 minutes to complete. Dinner will be ready at 5:30 p.m. Tina decides to time how long it takes to remove and clean one key and will then multiply that time by how many keys she needs to fix. She counts 15 keys that are sticky and times it to take 3 minutes to clean one. After Tina has cleaned one key, there are 14 left to clean. How many minutes total will it take for Tina to both clean the remaining keys and finish her assignment?"""
    # Define the time it takes to complete the assignment and the time it takes to clean one key
    ASSGN_TIME = 10
    KEY_CLEAN_TIME = 3

    # Calculate how long it will take to clean all the keys
    remaining_keys = 14
    time_to_clean_keys = remaining_keys * KEY_CLEAN_TIME

    # Calculate the total time needed
    total_time = ASSGN_TIME + time_to_clean_keys

    # Display the total time needed
    result = total_time
    return result

print(solution())