def solution():
    rice_amount = 50
    kept_ratio = 7/10
    
    # Calculate the amount of rice kept by Mr. Llesis
    kept_rice = rice_amount * kept_ratio

    # Calculate the amount of rice given to Mr. Everest
    given_rice = rice_amount - kept_rice

    # Calculate the difference between the amount of rice kept by Mr. Llesis and given to Mr. Everest
    difference = kept_rice - given_rice
    result = difference
    return result

print(solution())