def solution():
    """Three frogs are trying to hop across the road. The first frog takes 4 times as many hops as the second. The second frog takes twice as many as the third. If the three frogs took a total of 99 hops, how many hops did it take the second frog to cross the road?"""
    total_hops = 99
    first_frog_hops = 4 * second_frog_hops
    third_frog_hops = x
    second_frog_hops = third_frog_hops * 2
    
    total_hops = first_frog_hops + second_frog_hops + third_frog_hops
    second_frog_hops = (total_hops - first_frog_hops - third_frog_hops) / 2
    
    result = second_frog_hops
    return result

print(solution())