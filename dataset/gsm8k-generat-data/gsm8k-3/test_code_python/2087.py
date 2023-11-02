def solution():
    """A private company raised $2500 to be used for charity. They donated 80% to a public foundation with 8 organizations. How much money will each organization receive?"""
    # Calculate the total amount donated to the public foundation
    donation = 0.8 * 2500

    # Calculate the amount each organization will receive
    each_org = donation / 8

    # Display the amount each organization will receive
    result = each_org
    return result

print(solution())