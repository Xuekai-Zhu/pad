def solution():
    """There are 25 roses in a garden. There are 40 tulips. There are 35 daisies. What percentage of flowers are not roses?"""
    # Calculate the total number of flowers
    total_flowers = 25 + 40 + 35

    # Calculate the number of flowers that are not roses
    non_rose_flowers = total_flowers - 25

    # Calculate the percentage of flowers that are not roses
    non_rose_percentage = (non_rose_flowers / total_flowers) * 100

    # return the result
    result = non_rose_percentage
    return result

print(solution())