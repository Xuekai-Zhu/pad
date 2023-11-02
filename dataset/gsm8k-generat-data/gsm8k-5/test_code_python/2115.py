def solution():
    num_friends = 4  # Aku invited 4 friends
    num_packages = 3  # Aku's mother bought 3 packages of cookies
    cookies_per_package = 25  # Each package contains 25 cookies
    total_cookies = num_packages * cookies_per_package  # Aku has a total of 75 cookies

    # Calculate the number of cookies each child will eat
    cookies_per_child = total_cookies / (num_friends + 1)  # Aku is also eating, so divide by 5 instead of 4
    result = cookies_per_child
    return result

print(solution())