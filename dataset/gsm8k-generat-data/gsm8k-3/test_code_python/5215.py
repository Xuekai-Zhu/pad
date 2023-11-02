def solution():
    """Anya washes 32 hairs down the drain when she washes her hair and brushes out half that amount when she brushes it. How many hairs does Anya have to grow back to always have one more hair than she started with after washing, brushing, and growing it?"""
    # Define the number of hairs washed down the drain
    wash_loss = 32

    # Define the percentage of hairs lost when brushing
    brush_loss = 0.5

    # Calculate the number of hairs Anya needs to grow back
    total_loss = wash_loss + (wash_loss * brush_loss)
    extra_hair = 1
    total_hairs = (total_loss + extra_hair) / (1 - brush_loss)

    # Display the number of hairs Anya needs to grow back
    result = total_hairs
    return result

print(solution())