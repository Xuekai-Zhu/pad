def solution():
    brian_emmys = 6
    saoirse_emmys = 0
    combined_emmys = brian_emmys + saoirse_emmys
    prime = True
    # Check if combined_emmys is a prime number
    if combined_emmys < 2:
        prime = False
    else:
        for i in range(2, combined_emmys):
            if combined_emmys % i == 0:
                prime = False
                break
    if prime:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())