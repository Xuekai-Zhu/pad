def solution():
     cards_per_deck = 55
     cards_per_tear = 30
     tears_per_week = 3
     decks_purchased = 18
     
     total_cards_available = cards_per_deck * decks_purchased
     total_cards_tore = tears_per_week * cards_per_tear
     total_weeks = total_cards_available / total_cards_tore
     
     result = total_weeks
      
     return result

print(solution())