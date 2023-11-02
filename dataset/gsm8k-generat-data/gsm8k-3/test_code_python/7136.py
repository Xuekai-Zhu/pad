def solution():
    """Danny made chocolate cookies for his class and made sure each cookie had exactly 7 chips. He made 4 dozen in total. If the class eats half the cookies, how many chips are left uneaten?"""
    # Define the number of cookies Danny made
    cookies = 4 * 12

    # Calculate the total number of chips
    chips = cookies * 7

    # Calculate the number of chips eaten by the class
    eaten_chips = (cookies / 2) * 7

    # Calculate the number of chips left uneaten
    uneaten_chips = chips - eaten_chips

    # Display the number of chips left uneaten
    result = uneaten_chips
    return result

print(solution())