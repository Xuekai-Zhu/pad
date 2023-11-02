def solution():
    sister_age_now = 2 + 4  # Arman's sister is 2 years old four years ago
    arman_age_now = sister_age_now * 6  # Arman is six times older than his sister
    target_age = 40  # Arman wants to know how many years it will take him to reach 40 years old

    # Calculate how many years Arman needs to reach the target age
    years_to_target = target_age - arman_age_now
    result = years_to_target
    return result

print(solution())