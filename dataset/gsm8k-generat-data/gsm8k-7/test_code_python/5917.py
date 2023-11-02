def solution():
    starting_dogs = 80
    adopted_out_percent = 0.4
    taken_back = 5

    # Calculate the number of dogs adopted out
    adopted_out = starting_dogs * adopted_out_percent

    # Calculate the number of dogs in the shelter after adoption and taking back
    remaining_dogs = starting_dogs - adopted_out + taken_back
    result = remaining_dogs
    return result

print(solution())