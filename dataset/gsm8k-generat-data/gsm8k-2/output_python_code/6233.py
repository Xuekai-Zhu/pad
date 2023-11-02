def solution():
    """Three frogs are trying to hop across the road. The first frog takes 4 times as many hops as the second. The second frog takes twice as many as the third. If the three frogs took a total of 99 hops, how many hops did it take the second frog to cross the road?"""
    total_hops = 99
    third_frog_hops = 1
    second_frog_hops = third_frog_hops * 2
    first_frog_hops = second_frog_hops * 4
    total_frog_hops = first_frog_hops + second_frog_hops + third_frog_hops
    second_frog_cross_hops = total_hops - total_frog_hops
    result = second_frog_cross_hops
    return result

print(solution())