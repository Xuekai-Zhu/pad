def solution():
    cookies_per_batch = 12  # Each batch contains 12 cookies
    total_people = 4  # Kendra's family has 4 people
    batches = 3  # Kendra made 3 batches

    # Calculate the total number of cookies baked
    total_cookies = cookies_per_batch * batches

    # Calculate the total number of chocolate chips
    total_chocolate_chips = total_cookies * 2

    # Calculate the number of cookies each family member gets
    cookies_per_person = total_cookies / total_people

    # Calculate the number of chocolate chips each family member eats
    chips_per_person = total_chocolate_chips / total_people / cookies_per_person
    result = chips_per_person
    return result

print(solution())