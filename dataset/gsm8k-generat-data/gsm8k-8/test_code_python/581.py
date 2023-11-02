def solution():
    # Define the current age of the brother
    brother_age = 0

    # Loop through possible ages until the conditions are met
    while True:
        my_age = 2 * (brother_age + 10) - 10
        if my_age + brother_age == 45:
            result = my_age
            return result
        brother_age += 1

print(solution())