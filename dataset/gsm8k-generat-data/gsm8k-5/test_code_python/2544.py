def solution():
    largest_watermelon_weight = 8  # Michael's largest watermelon weighs 8 pounds
    clay_watermelon_weight = 3 * largest_watermelon_weight  # Clay's watermelon is three times larger than Michael's
    john_watermelon_weight = clay_watermelon_weight / 2  # John's watermelon is half the size of Clay's

    result = john_watermelon_weight
    return result

print(solution())