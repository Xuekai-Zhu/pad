def solution():
    """James is trying to create a new breed of kittens with extra-long tails. Each generation of kittens he breeds has a tail 25% longer than the last generation. If the first generation has tails 16 cm long, how long are the third generation's tails?"""
    first_gen_tail = 16
    percent_increase = 25
    second_gen_tail = first_gen_tail * (1 + (percent_increase / 100))
    third_gen_tail = second_gen_tail * (1 + (percent_increase / 100))
    result = third_gen_tail
    return result

print(solution())