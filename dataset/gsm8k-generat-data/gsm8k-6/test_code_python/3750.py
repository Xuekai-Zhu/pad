def solution():
    # Calculate the time required to make 12000 dolls
    doll_time = 12000 * 45  # each doll took 45 seconds to make
    # Calculate the time required to make the accessories for each doll
    accessory_time = 12000 * (2*10 + 3*10 + 1*10 + 5*10)  # 2 shoes, 3 bags, 1 set of cosmetics, and 5 hats for each doll, each accessory took 10 seconds to make
    # Calculate the total machine operation time required to manufacture all of the dolls and their accessories
    total_time = doll_time + accessory_time
    result = total_time
    return result

print(solution())