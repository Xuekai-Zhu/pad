def solution():
    """Suraya picked 12 apples more than Caleb, and Caleb picked 5 apples less than Kayla. If Kayla picked 20 apples, how many more apples did Suraya pick than Kayla?"""
    # Define the number of apples Kayla picked
    kayla_apples = 20

    # Calculate the number of apples Caleb picked
    caleb_apples = kayla_apples - 5

    # Calculate the number of apples Suraya picked
    suraya_apples = caleb_apples + 12

    # Calculate the difference between Suraya's and Kayla's apples
    difference = suraya_apples - kayla_apples

    # return the result
    result = difference
    return result

print(solution())