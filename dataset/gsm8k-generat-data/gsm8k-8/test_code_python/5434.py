def solution():
    total_apples = 340

    # Let x be the number of apples Kylie picked
    x = total_apples / 5

    # Calculate the number of apples Kayla picked
    kayla_apples = 10 + 4*x

    result = kayla_apples
    return result

print(solution())