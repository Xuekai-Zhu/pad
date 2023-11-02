def solution():
    
    starting_lollipops = 25
    kept_lollipops = 5
    remaining_lollipops = starting_lollipops - kept_lollipops
    friends = 4
    lollipops_per_friend = remaining_lollipops / friends
    result = lollipops_per_friend
    return result

print(solution())