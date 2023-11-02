def solution():
    staplers = 50  # There are 50 staplers in the stapler
    reports = 3 * 12  # Stacie staples 3 dozen (36) reports on her desk
    staplers_used = reports  # Each report requires one stapler

    # Calculate the number of staplers left in the stapler
    staplers_left = staplers - staplers_used
    result = staplers_left
    return result

print(solution())