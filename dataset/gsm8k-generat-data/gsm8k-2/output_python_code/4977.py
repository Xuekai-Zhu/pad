def solution():
    """Bob is going to plant corn in part of his garden. The rows are 120 feet long, and each seed needs its own dedicated space of 18 inches to its right. How many seeds can Bob plant in each row?"""
    row_length = 120 * 12  # convert feet to inches
    seed_space = 18  # inches
    total_space = row_length // seed_space  # integer division
    result = total_space
    return result

print(solution())