def solution():
    """Tony lifts weights as a form of exercise. He can lift 90 pounds with one arm in the exercise known as "the curl." 
    In an exercise known as "the military press," he can lift over his head twice the weight that he can curl. 
    His favorite exercise is known as "the squat" and he can squat 5 times the weight that he can lift in the military press. 
    How much weight, in pounds, can Tony lift in the squat exercise?"""
    # Define the weight that Tony can curl
    curl_weight = 90

    # Calculate the weight that Tony can lift in the military press
    military_press_weight = curl_weight * 2

    # Calculate the weight that Tony can lift in the squat exercise
    squat_weight = military_press_weight * 5

    result = squat_weight
    return result

print(solution())