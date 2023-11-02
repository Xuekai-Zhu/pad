def solution():
    num_tadpoles = 180
    percentage_kept = 0.25  # 75% let go

    # Calculate the number of tadpoles Trent let go
    num_let_go = num_tadpoles * percentage_kept

    # Calculate the number of tadpoles Trent kept
    num_kept = num_tadpoles - num_let_go
    result = num_kept
    return result

print(solution())