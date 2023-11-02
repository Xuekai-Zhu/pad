def solution():
    """Bob is going to plant corn in part of his garden. The rows are 120 feet long, and each seed needs its own dedicated space of 18 inches to its right. How many seeds can Bob plant in each row?"""
    row_length = 120 * 12  # convert feet to inches
    seed_spacing = 18
    available_space = row_length - seed_spacing  # leave 18 inches of space for the last seed on each row
    num_seeds = available_space // seed_spacing
    
    return num_seeds

print(solution())