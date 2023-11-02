def solution():
    # Calculate the total time taken to groom the dogs
    time_poodle = 30  # minutes taken to groom a poodle
    time_terrier = time_poodle / 2  # minutes taken to groom a terrier
    total_time = (time_poodle * 3) + (time_terrier * 8)  # total time taken to groom 3 poodles and 8 terriers
    result = total_time
    return result

print(solution())