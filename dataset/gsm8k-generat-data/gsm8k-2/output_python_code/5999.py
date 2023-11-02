def solution():
    """If it takes 8 days for 3 builders to build a cottage. How long will it take 6 builders to build the same size cottage working at the same rate?"""
    days = 8
    num_builders = 3
    same_rate_num_builders = 6
    same_size_time = (days * num_builders) / same_rate_num_builders
    result = same_size_time
    return result

print(solution())