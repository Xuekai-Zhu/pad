def solution():
    """Annie was given a pack of crayons. The pack contained 21 crayons. She already had a box of 36 crayons in her locker. Her friend Bobby gave her half the amount she already had in her locker. She decided to give her sister Mary 1/3 of her total amount of crayons. How many crayons does she give to Mary?"""
    # Define the initial number of crayons in Annie's locker
    initial_crayons = 36
 
    # Define the number of crayons in the pack she was given
    pack_crayons = 21

    # Bobby gives Annie half the amount she already had in her locker
    bobby_crayons = initial_crayons / 2

    # Calculate the total number of crayons Annie has now
    total_crayons = initial_crayons + pack_crayons + bobby_crayons

    # Calculate the number of crayons Annie gives to Mary
    mary_crayons = total_crayons / 3

    result = mary_crayons
    return result

print(solution())