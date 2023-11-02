def solution():
    """There are 25 roses in a garden. There are 40 tulips. There are 35 daisies. What percentage of flowers are not roses?"""
    # Define the total number of flowers
    total_flowers = 25 + 40 + 35

    # Calculate the percentage of flowers that are not roses
    not_roses_percentage = ((total_flowers - 25) / total_flowers) * 100

    result = not_roses_percentage
    return result

print(solution())