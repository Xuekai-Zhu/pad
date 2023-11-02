def solution():
    """Suraya picked 12 apples more than Caleb, and Caleb picked 5 apples less than Kayla. If Kayla picked 20 apples, how many more apples did Suraya pick than Kayla?"""
    # Define the number of apples picked by Kayla
    kayla_apples = 20

    # Calculate the number of apples picked by Caleb
    caleb_apples = kayla_apples - 5

    # Calculate the number of apples picked by Suraya
    suraya_apples = caleb_apples + 12

    # Calculate the difference between the number of apples picked by Suraya and Kayla
    difference = suraya_apples - kayla_apples

    # Display the difference
    result = difference
    return result

print(solution())