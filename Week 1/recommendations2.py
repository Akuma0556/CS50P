def main():
    difficulty = input("Difficult or Casual? ")
    if not (difficulty == "Difficult" or difficulty == "Casual"):
        print("Enter a valid difficulty")
        return
    
    mode = input("Multiplayer or Singleplayer? ")
    if not (mode == "Multiplayer" or mode == "Singleplayer"):
        print("Enter a valid mode")
        return
    
    if difficulty == "Difficult" and mode == "Multiplayer":
        recommend("Valorant")
    elif difficulty == "Difficult": # Must be Singleplayer due to guard clauses
        recommend("Dark Souls")
    elif mode == "Multiplayer":    # Must be Casual + Multiplayer
        recommend("Meccha Chameleon")
    else:                          # Must be Casual + Singleplayer
        recommend("Stardew Valley")
  
def recommend(game):
    print("You might like", game)


main()