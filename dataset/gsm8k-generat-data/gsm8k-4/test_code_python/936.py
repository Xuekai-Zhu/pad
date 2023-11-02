def solution():
    """Lizzie has half as many crayons as Bobbie. Bobbie has three times as many crayons as Billie. If Billie has 18 crayons, how many crayons does Lizzie have?"""
    # Define the number of crayons Billie has
    billie_crayons = 18

    # Calculate the number of crayons Bobbie has
    bobbie_crayons = 3 * billie_crayons

    # Calculate the number of crayons Lizzie has
    lizzie_crayons = bobbie_crayons / 2

    # Return the result
    result = lizzie_crayons
    return result

print(solution())