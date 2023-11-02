def solution():
    total_apples = 200  # Kayla and Kylie picked a total of 200 apples
    kylie_apples = total_apples / 1.25  # Kayla picked 1/4 of the apples that Kylie picked, so Kylie picked 1 - 1/4 = 3/4 of the apples
    kayla_apples = total_apples - kylie_apples  # Kayla and Kylie picked a total of 200 apples, so Kayla picked 200 - Kylie's apples
    result = kayla_apples
    return result

print(solution())