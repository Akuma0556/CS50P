def main():
    difficulty = input("Difficult or casual? ")
    mode = input("Multiplayer or Singleplayer? ")

    if difficulty == "Difficult":
        if mode == "Multiplayer":
            recommend("Valorant")
        elif mode == "Singleplayer":
            recommend("Dark Souls")
        else:
            print("Invalid input")
    elif difficulty == "Casual":
        if mode == "Multiplayer":
            recommend("Meccha Chameleon")
        elif mode == "Singleplayer":
            recommend("Stardew Valley")
    else:
        print("Invalid input")

def recommend(game):
    print("You might like", game)


main()