def solution():
    servings_per_pie = 8  # Each pie contains 8 servings
    apples_per_serving = 1.5  # Each serving requires 1.5 apples
    number_of_pies = 3  # Jessica is making 3 pies for her 12 guests

    # Calculate the total number of apples used in all the pies
    total_apples = servings_per_pie * apples_per_serving * number_of_pies

    # Calculate the average number of apples each guest will eat
    apples_per_guest = total_apples / 12
    result = apples_per_guest
    return result

print(solution())