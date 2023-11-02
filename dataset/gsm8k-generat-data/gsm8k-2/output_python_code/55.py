def solution():
    """There are 25 roses in a garden. There are 40 tulips. There are 35 daisies. What percentage of flowers are not roses?"""
    total_flowers = 25 + 40 + 35
    non_rose_flowers = total_flowers - 25
    percentage_non_rose = (non_rose_flowers / total_flowers) * 100
    result = percentage_non_rose
    return result

print(solution())