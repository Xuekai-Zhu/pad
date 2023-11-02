def solution():
    """Orlan gave one-fourth of his 20-meter rope to Allan. He then gave two-thirds of the remaining to Jack. How many meters of rope is left to Orlan?"""
    # Define the length of the rope and the fractions given away
    rope_length = 20
    fraction_allan = 1/4
    fraction_jack = 2/3

    # Calculate the length of rope given to Allan
    rope_allan = rope_length * fraction_allan

    # Calculate the length of rope remaining after giving to Allan
    rope_remaining = rope_length - rope_allan

    # Calculate the length of rope given to Jack
    rope_jack = rope_remaining * fraction_jack

    # Calculate the length of rope remaining after giving to Jack
    rope_left = rope_remaining - rope_jack

    # Display the length of rope left to Orlan
    result = rope_left
    return result

print(solution())