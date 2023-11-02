def solution():
    back_squat_weight = 200  # John used to back squat 200 kg
    front_squat_weight = back_squat_weight * 0.8  # John can front squat 80% as much as he back squats
    front_squat_weight_with_increase = back_squat_weight + 50  # John increased his back squat weight by 50 kg
    triple_weight = front_squat_weight * 0.9  # John can do a triple equal to 90% of the amount he front squats
    weight_moved = triple_weight * 3  # John will move the weight of three triples

    # Add the weight of the front squat after the back squat increase
    weight_moved += front_squat_weight_with_increase * 3

    result = weight_moved
    return result

print(solution())