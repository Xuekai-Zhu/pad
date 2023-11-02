def solution():
    # Calculate the total number of cookies baked by Kendra
    total_cookies = 12 * 3  # Kendra made 3 batches of cookies with 12 cookies in each batch
    # Calculate the total number of chocolate chips in all the cookies
    total_chips = total_cookies * 2 # Each cookie contains 2 chocolate chips
    # Calculate the number of chips each family member eats
    chips_per_person = total_chips / 4 # There are 4 people in Kendra's family
    result = chips_per_person
    return result

print(solution())