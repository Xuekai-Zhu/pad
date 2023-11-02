def solution():
    original_squat = 700
    original_bench = 400
    original_deadlift = 800

    squat_loss_percentage = 0.3  # 30% loss
    bench_loss_percentage = 0  # no loss
    deadlift_loss_weight = 200  # 200 pound loss

    # Calculate the new weight for squat
    squat_loss_weight = original_squat * squat_loss_percentage
    new_squat = original_squat - squat_loss_weight

    # Calculate the new weight for deadlift
    new_deadlift = original_deadlift - deadlift_loss_weight

    # Calculate the new total weight lifted
    new_total = new_squat + original_bench + new_deadlift
    result = new_total
    return result

print(solution())