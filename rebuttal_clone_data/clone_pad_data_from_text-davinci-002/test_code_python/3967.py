def solution():
    initial_roses = 2
    roses_traded = 1
    flowers_thrown_away = 0.5
    remaining_roses = initial_roses + roses_traded - flowers_thrown_away
    result = remaining_roses
    return result

print(solution())