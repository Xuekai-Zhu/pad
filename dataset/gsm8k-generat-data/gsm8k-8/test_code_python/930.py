def solution():
    # Calculate the number of apples each woman bought
    woman_apples = (30 + 20) / 2

    # Calculate the total number of apples bought by the women
    total_woman_apples = woman_apples * 3

    # Calculate the total number of apples bought by everyone
    total_apples = total_woman_apples + (30 * 2)

    result = total_apples
    return result

print(solution())