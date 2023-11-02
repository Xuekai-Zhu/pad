def solution():
    # Define Jefferson's number of bananas
    jefferson_bananas = 56

    # Calculate Walter's number of bananas
    walter_bananas = jefferson_bananas - (1/4 * jefferson_bananas)

    # Calculate the total number of bananas
    total_bananas = jefferson_bananas + walter_bananas

    # Calculate the number of bananas each gets
    bananas_each = total_bananas / 2

    # Calculate the number of bananas Walter gets
    walter_gets = bananas_each

    result = walter_gets
    return result

print(solution())