def solution():
    """Kylie and Kayla pick apples together and take home 340 apples total. If Kayla picked 10 more than 4 times the amount of apples that Kylie picked, how many apples did Kayla pick?"""
    total_apples = 340
    kylie_apples = total_apples / 2
    kayla_apples = 4 * kylie_apples + 10
    result = kayla_apples
    return result

print(solution())