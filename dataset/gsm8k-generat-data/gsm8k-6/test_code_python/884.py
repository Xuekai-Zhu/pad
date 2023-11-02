def solution():
    # Calculate the number of vampires after two nights
    initial_vampires = 2
    night_1_vampires = initial_vampires + (300 - initial_vampires) * 5  # first night each vampire turns 5 people into vampires
    night_2_vampires = night_1_vampires + (300 - night_1_vampires) * 5  # second night each vampire turns 5 more people into vampires
    total_vampires = night_2_vampires
    result = total_vampires
    return result

print(solution())