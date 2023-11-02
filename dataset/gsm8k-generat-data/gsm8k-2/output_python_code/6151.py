def solution():
    """Kayla and Kylie picked 200 apples total. Kayla picked 1/4 of the apples that Kylie picked. How many apples did Kayla pick?"""
    total_apples = 200
    kylie_apples = total_apples / 1.25
    kayla_apples = total_apples - kylie_apples
    result = kayla_apples
    return result

print(solution())