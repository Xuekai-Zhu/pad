def solution(): 
     initial_frogs = 5
     tadpoles = initial_frogs * 3
     surviving_tadpoles = tadpoles * (2/3)
     final_frogs = initial_frogs + surviving_tadpoles
     result = final_frogs - 8
     return result

print(solution())