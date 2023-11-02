def solution():
    """Kayla and Kylie picked 200 apples total. Kayla picked 1/4 of the apples that Kylie picked. How many apples did Kayla pick?"""
    total_apples = 200
    ky_apples = total_apples / 5  # Kylie picked 4/5 of the apples
    ka_apples = ky_apples / 4  # Kayla picked 1/4 of the apples Kylie picked
    result = ka_apples
    return result

print(solution())