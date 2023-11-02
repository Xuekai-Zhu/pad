def solution():
    total_apples = 340  # Kylie and Kayla picked 340 apples together

    # Let's assume that Kylie picked x apples
    # We know that Kayla picked 10 more than 4 times the amount of apples that Kylie picked
    # So, Kayla picked 4x + 10 apples
    # And we know that their total is 340
    # Therefore, we can write: x + (4x + 10) = 340
    # Simplifying and solving for x, we get x = 82.5

    kylie_apples = 82.5  # Kylie picked 82.5 apples
    kayla_apples = 4 * kylie_apples + 10  # Kayla picked 4 times the amount of apples that Kylie picked, plus 10
    result = kayla_apples
    return result

print(solution())