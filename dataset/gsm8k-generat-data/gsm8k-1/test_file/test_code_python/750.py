Unfortunately, the given question about Samantha's last name seems to be incomplete as there is no information provided about Bobbie's last name or Jamie's last name beyond "Jamie Grey". Therefore, we cannot provide a solution for this question.

def solution():
    """Lorraine and Colleen are trading stickers for buttons. Each large sticker is worth a large button or three small buttons. A small sticker is worth one small button. A large button is worth three small stickers. Lorraine starts with 30 small stickers and 40 large stickers. She trades 90% of her small stickers for large buttons. She trades 50% of her large stickers for large buttons and trades the rest of them for small buttons. How many buttons does she have by the end?"""
    small_stickers_start = 30
    large_stickers_start = 40
    large_sticker_to_large_button = 1
    large_sticker_to_small_button = 3
    small_sticker_to_small_button = 1
    large_button_to_small_sticker = 3
    
    # Calculate number of large buttons and small buttons from initial stickers
    large_buttons = large_stickers_start * large_sticker_to_large_button
    small_buttons = small_stickers_start * small_sticker_to_small_button
    
    # Calculate number of large buttons from traded small stickers
    large_buttons_from_small_stickers = int(small_stickers_start * 0.9) * large_sticker_to_large_button
    
    # Calculate number of large buttons from traded large stickers
    large_stickers_traded = int(large_stickers_start * 0.5)
    large_buttons_from_large_stickers = large_stickers_traded * large_sticker_to_large_button
    
    # Calculate number of small buttons from remaining large stickers
    large_stickers_remaining = large_stickers_start - large_stickers_traded
    small_buttons_from_large_stickers = large_stickers_remaining * large_sticker_to_small_button
    
    # Calculate number of small stickers from remaining large buttons
    large_buttons_remaining = large_buttons - (large_buttons_from_small_stickers + large_buttons_from_large_stickers)
    small_stickers_from_large_buttons = large_buttons_remaining * large_button_to_small_sticker
    
    # Calculate total number of buttons
    total_large_buttons = large_buttons + large_buttons_from_small_stickers + large_buttons_from_large_stickers
    total_small_buttons = small_buttons + small_buttons_from_large_stickers + small_stickers_from_large_buttons
    
    result = total_large_buttons + total_small_buttons
    return result

print(solution())