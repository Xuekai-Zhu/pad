def solution():
    football_field_length = 100  # The football field is 100 yards long
    blake_runs_per_minute = 15  # Blake runs back and forth 15 times
    kelly_runs_per_minute = 1  # Kelly runs back and forth once
    total_blake_runs = blake_runs_per_minute * 34  # Blake runs for 34 times
    total_kelly_runs = kelly_runs_per_minute * 34  # Kelly runs for 34 times

    # Calculate the total time Blake spends running
    total_blake_time = blake_runs_per_minute * total_blake_runs

    # Calculate the total time Kelly spends running
    total_kelly_time = kelly_runs_per_minute * total_kelly_runs

    # Calculate the total time the winner spends running
    total_winner_time = total_blake_time + total_kelly_time - total_winner_time

    # Calculate the difference

print(solution())