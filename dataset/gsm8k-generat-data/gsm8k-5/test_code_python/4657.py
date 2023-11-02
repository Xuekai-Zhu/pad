def solution():
    initial_size = 100  # The cloth is initially 100 square inches
    donated_size = 0  # Keep track of how much cloth is donated after each cut

    # Cut the cloth in half twice and donate one half each time
    for i in range(2):
        donated_size += initial_size / 2
        initial_size = initial_size / 2

    result = donated_size
    return result

print(solution())