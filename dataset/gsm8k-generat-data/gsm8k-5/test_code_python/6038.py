def solution():
    megan_candy = 5  # Megan has 5 pieces of candy
    mary_candy = 3*megan_candy  # Mary has 3 times as much candy as Megan
    mary_candy += 10  # Mary adds 10 more pieces of candy to her collection

    # Calculate the total number of candies Mary has in total
    total_candy = mary_candy + megan_candy
    result = total_candy
    return result

print(solution())