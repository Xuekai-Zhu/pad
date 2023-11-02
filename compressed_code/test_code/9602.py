def solution():
    
    kit_kats = 5
    hershey_kisses = kit_kats * 3
    nerds = 8
    lollipops = 11
    baby_ruths = 10
    reeses = baby_ruths / 2
    total_candy = kit_kats + hershey_kisses + nerds + lollipops + baby_ruths + reeses
    total_candy -= 5 
    result = total_candy
    return result

print(solution())