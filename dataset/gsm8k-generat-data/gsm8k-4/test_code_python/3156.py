def solution():
    """Kendra baked cookies for her family. Each batch contains 12 cookies. His family has 4 total people. She made three batches. Each cookie contains 2 chocolate chips. How many chips does each family member eat if they all get the same number of cookies?"""
    # Define the number of batches and cookies per batch
    num_batches = 3
    cookies_per_batch = 12

    # Calculate the total number of cookies
    total_cookies = num_batches * cookies_per_batch

    # Calculate the total number of chocolate chips
    total_chips = total_cookies * 2

    # Calculate the number of chips per family member
    num_people = 4
    chips_per_person = total_chips / num_people

    # Return the result
    result = chips_per_person
    return result

print(solution())