def solution():
    """Annie was given a pack of crayons. The pack contained 21 crayons. She already had a box of 36 crayons in her locker. Her friend Bobby gave her half the amount she already had in her locker. She decided to give her sister Mary 1/3 of her total amount of crayons. How many crayons does she give to Mary?"""
    # Define the number of crayons in the pack and in Annie's locker
    pack_crayons = 21
    locker_crayons = 36

    # Calculate the number of crayons Bobby gave her
    bobby_crayons = locker_crayons / 2

    # Calculate the total number of crayons Annie has
    total_crayons = pack_crayons + locker_crayons + bobby_crayons

    # Calculate the number of crayons Annie gives to Mary
    mary_crayons = total_crayons / 3

    # Display the number of crayons Annie gives to Mary
    result = mary_crayons
    return result

print(solution())