def solution():
    akeno_spent = 2985  # Akeno spent $2985 to furnish his apartment
    lev_spent = akeno_spent / 3  # Lev spent one-third of what Akeno spent
    ambrocio_spent = lev_spent - 177  # Ambrocio spent $177 less than Lev

    # Calculate the total amount spent by Lev and Ambrocio combined
    combined_spending = lev_spent + ambrocio_spent

    # Calculate how much more Akeno spent than the other two combined
    difference = akeno_spent - combined_spending
    result = difference
    return result

print(solution())