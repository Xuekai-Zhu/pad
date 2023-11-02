def solution():
    # Calculate the number of dogs Harly adopts out and takes back
    adopted_dogs = 0.4 * 80  # 40% of the 80 dogs are adopted out
    taken_back_dogs = 5

    # Calculate the total number of dogs Harly has now
    total_dogs = 80 - adopted_dogs + taken_back_dogs
    result = total_dogs
    return result

print(solution())