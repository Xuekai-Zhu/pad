def solution():
    total_pizza = 2
    bob_pizza = total_pizza / 2
    tom_pizza = total_pizza / 3
    sally_pizza = total_pizza / 6
    jerry_pizza = total_pizza / 4
    total_slices = total_pizza * 12
    total_eaten = bob_pizza + tom_pizza + sally_pizza + jerry_pizza
    slices_leftover = total_slices - total_eaten
    result = slices_leftover
    return result

print(solution())