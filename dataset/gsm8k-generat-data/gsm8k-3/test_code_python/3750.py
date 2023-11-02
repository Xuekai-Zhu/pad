def solution():
    """Last month, a factory made 12000 dolls and their associated accessories.  The accessories for each doll included 2 shoes, 3 bags, 1 set of cosmetics, and 5 hats.  If each doll took 45 seconds to make and each accessory took 10 seconds to make, what was the total combined machine operation time, in seconds, required to manufacture all of the dolls and their accessories?"""
    # Define the number of dolls and their accessories
    NUM_DOLLS = 12000
    NUM_SHOES = 2 * NUM_DOLLS
    NUM_BAGS = 3 * NUM_DOLLS
    NUM_COSMETICS = NUM_DOLLS
    NUM_HATS = 5 * NUM_DOLLS

    # Calculate the machine operation time for the dolls and their accessories
    doll_time = NUM_DOLLS * 45
    shoe_time = NUM_SHOES * 10
    bag_time = NUM_BAGS * 10
    cosmetic_time = NUM_COSMETICS * 10
    hat_time = NUM_HATS * 10
    total_time = doll_time + shoe_time + bag_time + cosmetic_time + hat_time

    # Display the total machine operation time
    result = total_time
    return result

print(solution())