def solution():
    """Anya washes 32 hairs down the drain when she washes her hair and brushes out half that amount when she brushes it. How many hairs does Anya have to grow back to always have one more hair than she started with after washing, brushing, and growing it?"""
    # Define the initial number of hairs
    initial_hairs = None

    # Define the number of hairs washed down the drain
    washed_hairs = 32

    # Define the number of hairs brushed out
    brushed_hairs = washed_hairs / 2

    # Calculate the number of hairs that need to grow back in order for Anya to have one more hair than she started with
    total_hairs = initial_hairs - washed_hairs - brushed_hairs + 1

    result = total_hairs
    return result

print(solution())