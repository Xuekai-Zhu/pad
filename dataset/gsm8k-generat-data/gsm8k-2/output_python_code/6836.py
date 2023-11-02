def solution():
    """Annie was given a pack of crayons. The pack contained 21 crayons. She already had a box of 36 crayons in her locker. Her friend Bobby gave her half the amount she already had in her locker. She decided to give her sister Mary 1/3 of her total amount of crayons. How many crayons does she give to Mary?"""
    pack_crayons = 21
    locker_crayons = 36
    bobby_crayons = locker_crayons / 2
    total_crayons = pack_crayons + locker_crayons + bobby_crayons
    mary_crayons = total_crayons / 3
    result = mary_crayons
    return result

print(solution())