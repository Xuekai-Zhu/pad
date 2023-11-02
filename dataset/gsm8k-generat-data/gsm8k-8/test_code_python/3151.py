def solution():
    # Let x be Jason's initial amount of money
    # First, calculate how much money Jason had after buying books
    x -= x/4 + 10
    # Then, calculate how much money Jason had after buying DVDs
    x -= 2/5 * x + 8
    # Finally, set the remaining money equal to $130 and solve for x
    x = 130 + x
    result = x
    return result

print(solution())