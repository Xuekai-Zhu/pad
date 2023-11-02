def solution():
    
    buttered_popcorn = 12
    caramel_popcorn = 10
    alan_buttered_popcorn = 3
    alan_caramel_popcorn = 1
    total_popcorn = buttered_popcorn + caramel_popcorn
    alan_popcorn = alan_buttered_popcorn + alan_caramel_popcorn
    remaining_popcorn = total_popcorn - alan_popcorn
    result = remaining_popcorn
    return result

print(solution())