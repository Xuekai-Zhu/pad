def solution():
    """Kendra baked cookies for her family. Each batch contains 12 cookies. His family has 4 total people. She made three batches. Each cookie contains 2 chocolate chips. How many chips does each family member eat if they all get the same number of cookies?"""
    cookies_per_batch = 12
    total_people = 4
    num_batches = 3
    total_cookies = cookies_per_batch * num_batches
    total_chips = total_cookies * 2
    chips_per_person = total_chips / total_people
    result = chips_per_person
    return result

print(solution())