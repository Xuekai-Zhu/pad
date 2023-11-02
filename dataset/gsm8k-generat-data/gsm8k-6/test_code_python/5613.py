def solution():
    # Calculate the number of pictures that can be held with 6 megabytes each
    num_pictures = (3000 * 8) / 6
    result = int(num_pictures)  # round down to nearest integer
    return result

print(solution())