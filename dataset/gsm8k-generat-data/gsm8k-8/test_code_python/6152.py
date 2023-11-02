def solution():
    # Define the total number of apples
    total_apples = 200

    # Calculate the fraction of apples that Kayla picked (1/4 of the apples Kylie picked)
    kayla_fraction = 1/4
    kylie_fraction = 1 - kayla_fraction

    # Calculate the number of apples that Kylie picked
    kylie_apples = total_apples * kylie_fraction

    # Calculate the number of apples that Kayla picked
    kayla_apples = total_apples * kayla_fraction

    result = kayla_apples
    return result

print(solution())