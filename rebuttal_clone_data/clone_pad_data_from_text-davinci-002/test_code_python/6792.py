def solution():
     labrador_weight = 40
     dachshund_weight = 12
     labrador_gain = labrador_weight * 0.25
     dachshund_gain = dachshund_weight * 0.25
     labrador_final = labrador_weight + labrador_gain
     dachshund_final = dachshund_weight + dachshund_gain
     difference = labrador_final - dachshund_final
     result = difference
     return result

print(solution())