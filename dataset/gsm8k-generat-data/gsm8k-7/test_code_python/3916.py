def solution():
    thomas_saving = 40 * 12 * 6  # Thomas has been saving $40 every month for 6 years
    joseph_saving = (3/5) * 40  # Joseph has been saving 2/5 times less than Thomas per month
    joseph_total_saving = joseph_saving * 12 * 6  # Calculate Joseph's total savings in 6 years
    total_saving = thomas_saving + joseph_total_saving  # Calculate the total savings of both Thomas and Joseph
    result = total_saving
    return result

print(solution())