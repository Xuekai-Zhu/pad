def solution():
    # Calculate the number of pieces of candy Harper collected
    maggie_candy = 50
    harper_candy = maggie_candy * 1.3  # Harper collected 30% more candy than Maggie

    # Calculate the number of pieces of candy Neil collected
    neil_candy = harper_candy * 1.4  # Neil collected 40% more candy than Harper
    result = neil_candy
    return result

print(solution())