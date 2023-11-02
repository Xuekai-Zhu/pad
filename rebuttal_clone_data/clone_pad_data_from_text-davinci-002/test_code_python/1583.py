def solution():
    new_computer_cost = 600
    new_computer_life = 6
    two_used_computers_cost = 200 * 2
    used_computer_life = 3
    total_cost_new_computer = new_computer_cost * new_computer_life
    total_cost_two_used_computers = two_used_computers_cost * used_computer_life
    difference = total_cost_new_computer - total_cost_two_used_computers
    result = difference
    return result

print(solution())