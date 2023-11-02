def solution():
    # Calculate the total distance John drove
    total_distance = 150 + 50 + 50  # his normal trip is 150 miles, he drove 50 miles out of the way and had to drive 50 miles back on track

    # Calculate the total time John spent driving
    time = (total_distance / 50) * 3  # he would take 3 hours to drive 150 miles at a speed of 50 miles per hour
    result = time
    return result

print(solution())