def solution():
    
    num_grandchildren = 3
    hat_wool = 2
    scarf_wool = 4
    sweater_wool = 12
    mittens_wool = 1
    socks_wool = 2
    total_wool = (hat_wool + scarf_wool + sweater_wool + mittens_wool + socks_wool) * num_grandchildren
    result = total_wool
    return result

print(solution())