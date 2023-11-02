def solution():
    """Suraya picked 12 apples more than Caleb, and Caleb picked 5 apples less than Kayla.
    If Kayla picked 20 apples, how many more apples did Suraya pick than Kayla?"""
    kayla_apples = 20
    caleb_apples = kayla_apples - 5
    suraya_apples = caleb_apples + 12
    difference = suraya_apples - kayla_apples
    result = difference
    return result

print(solution())