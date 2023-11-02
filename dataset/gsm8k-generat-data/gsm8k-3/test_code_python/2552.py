def solution():
    """Dina has twice as many dolls as Ivy. 2/3 of Ivy's dolls are collectors editions. If Ivy has 20 collectors edition dolls, how many dolls does Dina have?"""
    # Define the number of collectors edition dolls Ivy has
    ivy_collectors = 20

    # Calculate the total number of dolls Ivy has
    ivy_total = ivy_collectors / (2/3)

    # Calculate the total number of dolls Dina has
    dina_total = ivy_total * 2

    # Display the total number of dolls Dina has
    result = dina_total
    return result

print(solution())