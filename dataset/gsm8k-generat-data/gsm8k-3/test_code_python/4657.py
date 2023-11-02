def solution():
    """Fatima has a piece of cloth that is 100 square inches big. She has decided to cut the cloth in half. She plans on keeping half and donating the other half. If she does this 2 times, then how much cloth will she have donated?"""
    # Define the starting area of the cloth
    initial_area = 100

    # Calculate the area after the first cut
    half_area = initial_area / 2

    # Calculate the area after the second cut
    quarter_area = half_area / 2

    # Calculate the total amount of cloth donated
    donated_area = half_area + quarter_area

    # Display the donated area
    result = donated_area
    return result

print(solution())