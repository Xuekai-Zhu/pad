def solution():
    total_age = 40 * 3  # The total average age of three friends is 40
    molly_age = 30  # Molly's age is 30
    combined_age_of_jared_and_hakimi = total_age - molly_age  # The combined age of Jared and Hakimi is total_age minus Molly's age
    # Let x be Hakimi's age
    # Then Jared's age is x + 10
    # The sum of their ages is combined_age_of_jared_and_hakimi
    # x + (x + 10) = combined_age_of_jared_and_hakimi
    # Solving for x, we get
    hakimi_age = (combined_age_of_jared_and_hakimi - 10) / 2
    result = hakimi_age
    return result

print(solution())