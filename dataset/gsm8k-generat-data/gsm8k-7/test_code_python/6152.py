def solution():
    total_apples = 200
    kylie_ratio = 4
    kayla_ratio = 1

    # Calculate the total number of apples that Kylie picked
    kylie_apples = total_apples / (kylie_ratio + kayla_ratio) * kylie_ratio

    # Calculate the total number of apples that Kayla picked
    kayla_apples = total_apples - kylie_apples
    result = kayla_apples
    return result

print(solution())