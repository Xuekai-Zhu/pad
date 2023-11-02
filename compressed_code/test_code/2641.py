def solution():
    
    total_weight = 239
    ron_lift = 1  
    roger_lift = (ron_lift * 4) - 7
    rodney_lift = roger_lift * 2
    while rodney_lift + roger_lift + ron_lift != total_weight:
        ron_lift += 1
        roger_lift = (ron_lift * 4) - 7
        rodney_lift = roger_lift * 2
    result = rodney_lift
    return result

print(solution())