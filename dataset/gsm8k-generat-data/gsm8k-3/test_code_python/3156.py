def solution():
    """Kendra baked cookies for her family. Each batch contains 12 cookies. His family has 4 total people. She made three batches. Each cookie contains 2 chocolate chips. How many chips does each family member eat if they all get the same number of cookies?"""
    # Define the number of people in the family and the number of batches made
    people = 4
    batches = 3

    # Calculate the total number of cookies
    total_cookies = batches * 12

    # Calculate the total number of chocolate chips
    total_chips = total_cookies * 2

    # Calculate the number of chips each family member eats
    chips_per_person = total_chips / people

    # Display the number of chips each family member eats
    result = chips_per_person
    return result

print(solution())