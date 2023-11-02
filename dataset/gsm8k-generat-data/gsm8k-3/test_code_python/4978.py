def solution():
    """Bob is going to plant corn in part of his garden. The rows are 120 feet long, and each seed needs its own dedicated space of 18 inches to its right. How many seeds can Bob plant in each row?"""
    # Convert rows length from feet to inches
    row_length_inches = 120 * 12

    # Calculate the number of 18 inch spaces in each row
    num_spaces = row_length_inches // 18

    # Calculate the number of seeds that can be planted in each row
    num_seeds = num_spaces - 1

    # Display the number of seeds that can be planted in each row
    result = num_seeds
    return result

print(solution())