def solution():
    """One hundred chips were divided by Ian and Lyle in the ratio 4:6. What percentage of the chips did Lyle have?"""
    # Define the total number of chips
    total_chips = 100

    # Calculate the fraction of chips that Ian has
    ian_fraction = 4 / (4 + 6)

    # Calculate the number of chips that Ian has
    ian_chips = total_chips * ian_fraction

    # Calculate the number of chips that Lyle has
    lyle_chips = total_chips - ian_chips

    # Calculate the percentage of chips that Lyle has
    lyle_percentage = (lyle_chips / total_chips) * 100

    # Round the answer to the nearest whole number
    result = round(lyle_percentage)

    return result

print(solution())