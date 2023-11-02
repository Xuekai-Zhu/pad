def solution():
    jason_arm_tattoos = 2  # Jason has two tattoos on each arm
    jason_leg_tattoos = 3  # Jason has three tattoos on each leg
    jason_total_tattoos = jason_arm_tattoos * 2 + jason_leg_tattoos * 2  # Calculate Jason's total number of tattoos 

    adam_tattoos = 2 * jason_total_tattoos + 3  # Adam has three more than twice as many tattoos as Jason
    result = adam_tattoos
    return result

print(solution())