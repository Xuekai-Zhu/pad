def solution():
    """Sam shared a sum of money between his three cousins Sandra, Amy and Ruth in the ratio 2:1:3 respectively. If Amy got $50, how much did Sandra get?"""
    # Since Amy got 1 part out of a total of 6 parts (2+1+3=6) of the money,
    # we can find out the value of 1 part and then multiply it by 2 to find out Sandra's share.
    amy_share = 50
    amy_parts = 1
    total_parts = 6
    amy_part_value = amy_share / amy_parts
    sandra_parts = 2
    sandra_share = sandra_parts * amy_part_value
    result = sandra_share
    
    return result

print(solution())