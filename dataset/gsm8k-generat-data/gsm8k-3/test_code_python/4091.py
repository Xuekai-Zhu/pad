def solution():
    """Ryan works in an office that has an even number of men and women working there.  Ryan participates in a meeting composed of 4 men and 6 women who are pulled from the office floor.   This reduces the number of women working on the office floor by 20%.  How many people work at Ryan's office?"""
    # Let's assume that the number of men and women in the office is equal, and let's call this number x
    # The total number of people in the office is then 2x

    # We know that 4 men and 6 women were pulled from the office floor for the meeting
    # This means that there are x-4 men and x-6 women still working on the office floor

    # We also know that the number of women working on the office floor was reduced by 20%
    # This means that there are 0.8(x-6) women still working on the office floor

    # We can now set up an equation based on the fact that there are an equal number of men and women in the office
    # 0.8(x-6) = x-4

    # Solving for x gives us:
    x = 32

    # Therefore, the total number of people in the office is 2x, which is:
    total_people = 64

    # Display the total number of people in the office
    result = total_people
    return result

print(solution())