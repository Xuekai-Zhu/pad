def solution():
    """At a CD store, 40% of the CDs cost $10 each, and the rest cost $5 each. Prince bought half the CDs sold at $10 each, and all of the CDs sold at $5 each. If the total number of CDs was 200, how much money did Prince spend on buying the CDs?"""
    # Determine the number of CDs sold at $10 and $5 each
    num_cd_10 = int(0.4 * 200)
    num_cd_5 = 200 - num_cd_10

    # Determine the number of CDs Prince bought at $10 and $5 each
    num_cd_10_prince = int(num_cd_10 / 2)
    num_cd_5_prince = num_cd_5

    # Calculate the total cost of the CDs Prince bought
    total_cost = (num_cd_10_prince * 10) + (num_cd_5_prince * 5)

    # Display the total cost
    result = total_cost
    return result

print(solution())