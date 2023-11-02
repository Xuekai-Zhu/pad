def solution():
    # Define the status of English and Japanese serfs
    english_serf_status = "harshly treated with little legal redress"
    japanese_serf_status = "viewed as essential to society"
    # Compare the status of English and Japanese serfs
    if japanese_serf_status > english_serf_status:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())