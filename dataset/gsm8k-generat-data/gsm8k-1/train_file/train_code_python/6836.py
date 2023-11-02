def solution():
    """Annie was given a pack of crayons. The pack contained 21 crayons. She already had a box of 36 crayons in her locker. Her friend Bobby gave her half the amount she already had in her locker. She decided to give her sister Mary 1/3 of her total amount of crayons. How many crayons does she give to Mary?"""
    crayons_pack = 21
    crayons_locker = 36
    friend_crayons = crayons_locker / 2
    total_crayons = crayons_pack + crayons_locker + friend_crayons
    mary_crayons = total_crayons / 3
    result = mary_crayons
    return result

print(solution())