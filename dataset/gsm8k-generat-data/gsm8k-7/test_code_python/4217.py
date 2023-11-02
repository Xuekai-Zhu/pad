def solution():
    num_tourists = 30
    num_eaten_by_anacondas = 2
    num_poisoned_by_frogs = (num_tourists - num_eaten_by_anacondas) / 2
    num_recovered_from_poison = num_poisoned_by_frogs / 7
    num_left_at_end = num_tourists - num_eaten_by_anacondas - num_poisoned_by_frogs + num_recovered_from_poison
    result = num_left_at_end
    return result

print(solution())