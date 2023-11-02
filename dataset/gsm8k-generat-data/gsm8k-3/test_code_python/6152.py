def solution():
    """Kayla and Kylie picked 200 apples total. Kayla picked 1/4 of the apples that Kylie picked. How many apples did Kayla pick?"""
    # Define the total number of apples picked
    total_apples = 200

    # Define the ratio of apples picked by Kayla to Kylie
    kayla_to_kylie = 1/4

    # Calculate the total number of apples picked by Kylie
    kylie_apples = total_apples / (1 + kayla_to_kylie)

    # Calculate the number of apples picked by Kayla
    kayla_apples = kayla_to_kylie * kylie_apples

    # Display the number of apples picked by Kayla
    result = kayla_apples
    return result

print(solution())