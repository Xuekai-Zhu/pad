def solution():
    
    kit_kat = 5
    hershey_kisses = 3 * kit_kat
    nerds = 8
    lollipops = 11
    baby_ruth = 10
    reese_pb_cups = baby_ruth / 2
    total_candy = kit_kat + hershey_kisses + nerds + lollipops + baby_ruth + reese_pb_cups
    total_candy -= 5  
    result = total_candy
    return result

print(solution())