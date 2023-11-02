def solution():
    batch_size = 12
    num_people = 4
    num_batches = 3
    chips_per_cookie = 2

    # Calculate the total number of cookies Kendra baked
    total_cookies = batch_size * num_batches

    # Calculate the total number of chocolate chips in all the cookies
    total_chips = total_cookies * chips_per_cookie

    # Calculate the number of chips each family member eats
    chips_per_person = total_chips / num_people
    result = chips_per_person
    return result

print(solution())