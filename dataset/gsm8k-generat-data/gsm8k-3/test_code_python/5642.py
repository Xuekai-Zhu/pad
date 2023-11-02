def solution():
    """Christine and Rachel went strawberry picking.  They want to make pies and need 3 pounds of strawberries per pie.
    Christine picked 10 pounds of strawberries and Rachel picked twice as much as Rachel.  Together, how many pies can they make?"""
    # Define the number of pounds of strawberries needed per pie
    STRAWBERRY_PER_PIE = 3

    # Define the number of pounds of strawberries picked by each person
    christine_pounds = 10
    rachel_pounds = christine_pounds * 2

    # Calculate the total number of pies they can make
    total_pies = (christine_pounds + rachel_pounds) // STRAWBERRY_PER_PIE

    # Display the total number of pies they can make
    result = total_pies
    return result

print(solution())