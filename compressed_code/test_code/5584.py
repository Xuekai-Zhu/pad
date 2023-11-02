def solution():
    
    initial_gum = 10
    additional_gum = 3
    total_gum = initial_gum + additional_gum
    friends = 11
    gum_given_away = friends * 1
    remaining_gum = total_gum - gum_given_away
    result = remaining_gum
    return result

print(solution())