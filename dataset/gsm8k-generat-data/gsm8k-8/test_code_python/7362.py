def solution():
    # Define the age of the third boy
    third_boy_age = 11

    # Calculate the sum of the ages of the two same-aged boys
    same_ages_sum = 29 - third_boy_age

    # Divide the same-aged sum by 2 to get the age of each same-aged boy
    same_age = same_ages_sum / 2

    result = same_age
    return result

print(solution())