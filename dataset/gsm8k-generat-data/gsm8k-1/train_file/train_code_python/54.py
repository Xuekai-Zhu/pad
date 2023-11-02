def solution():
    """There are 25 roses in a garden. There are 40 tulips. There are 35 daisies. What percentage of flowers are not roses?"""
    total_flowers = 25 + 40 + 35
    roses = 25
    non_roses = total_flowers - roses
    percentage_non_roses = (non_roses / total_flowers) * 100
    result = percentage_non_roses
    return result

print(solution())