def solution():
    blocks_used = 0
 
    stack_one = 7
    stack_two = stack_one + 3
    stack_three = stack_two - 6
    stack_four = stack_three + 10
    stack_five = stack_two * 2
 
    blocks_used = stack_one + stack_two + stack_three + stack_four + stack_five
 
    return blocks_used

print(solution())