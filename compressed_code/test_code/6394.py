def solution():
    
    num_parrots = 8
    num_snakes = num_parrots * 3
    num_monkeys = num_snakes * 2
    num_elephants = (num_parrots + num_snakes) / 2
    num_zebras = num_elephants - 3
    num_difference = num_zebras - num_monkeys
    result = abs(num_difference)  
    
    return result

print(solution())