def solution():
    """Last month, a factory made 12000 dolls and their associated accessories.  The accessories for each doll included 2 shoes, 3 bags, 1 set of cosmetics, and 5 hats.  If each doll took 45 seconds to make and each accessory took 10 seconds to make, what was the total combined machine operation time, in seconds, required to manufacture all of the dolls and their accessories?"""
    # Define the number of dolls
    num_dolls = 12000

    # Calculate the number of accessories for each doll
    num_shoes = 2
    num_bags = 3
    num_cosmetics = 1
    num_hats = 5

    # Calculate the total number of accessories
    num_accessories = num_dolls * (num_shoes + num_bags + num_cosmetics + num_hats)

    # Calculate the time required to make each doll and accessory
    doll_time = 45
    accessory_time = 10

    # Calculate the total machine operation time
    total_time = (num_dolls * doll_time) + (num_accessories * accessory_time)

    # return the result
    return total_time

print(solution())