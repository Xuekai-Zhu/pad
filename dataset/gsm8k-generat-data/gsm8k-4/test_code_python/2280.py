def solution():
    """Orlan gave one-fourth of his 20-meter rope to Allan. He then gave two-thirds of the remaining to Jack. How many meters of rope is left to Orlan?"""
    # Define the initial length of the rope
    initial_length = 20

    # Calculate the length of the rope given to Allan
    allan_length = initial_length * 0.25

    # Calculate the remaining length of the rope
    remaining_length = initial_length - allan_length

    # Calculate the length of the rope given to Jack
    jack_length = remaining_length * (2/3)

    # Calculate the length of the rope left to Orlan
    orlan_length = remaining_length - jack_length

    # return the result
    result = orlan_length
    return result

print(solution())