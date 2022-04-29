#Hangman Program Using Dictionary
import random

def playHangman():
    #Reads file full of available hangman words
    #and splits them up using whitespace
    infile = open("words.txt", "r")
    words = infile.read()
    words = words.split()
    #Chooses a random word and creates list of solved word letters,
    #list of unsolved list characters, and dictionary for word's letters
    word = words[random.randint(0, len(words) - 1)]
    unsolvedList = []
    solvedList = []
    solvedDict = {}
    guessedLetters = [] #maps letters : list of index(es) for that letter
    #Populates solved list with each letter in word and unsolved list
    #with underscorse to represent unguesses letters
    for c in word:
        solvedList.append(c)
        unsolvedList.append("_")
    #Populates dictionary with empty lists mapped to each letter in the word
    for c in solvedList:
        solvedDict[c] = []
    #Populates empty lists with the index(es) for the position of each letter
    for i in range(len(solvedList)):
        solvedDict[solvedList[i]].append(i)
    guesses = 6
    print("Type in quit to end the game")
    print("")
    while True:
        #Prints how much of the list is solved and prompts user to guess letter
        for c in unsolvedList:
            print(c, end = ' ')
        guess = input("Guess a letter: ")
        #If user types in quit, quits the game
        if guess == "quit":
            print("You ended the game")
            break
        #Doesn't accept invalid inputs like numbers and words, asking for
        #another guess
        while len(guess) != 1 or guess.isalpha() == False:
            print("Invalid guess")
            print("")
            guess = input("Guess a letter: ")
        #If letter was already guessed, tells user to guess a different letter
        if guess in guessedLetters:
            print("You already guessed this letter")
            print("")
        #If valid guess, changes unsolved list and adds guessed letter to list
        #of guessed letters
        elif guess in solvedDict:
            print("")
            guessedLetters.append(guess)
            for letterPosition in solvedDict[guess]:
                unsolvedList.pop(letterPosition)
                unsolvedList.insert(letterPosition, guess)
            #If word has been fully guessed, ends the game
            if "_" not in unsolvedList:
                for c in unsolvedList:
                    print(c, end = ' ')
                print("You won")
                print("The correct word was ", word)
                break
        #If guessed letter not in word, decrements guesses
        else:
            guessedLetters.append(guess)
            guesses -= 1
            #If 0 guesses remain, user loses
            if guesses <= 0:
                print("You lost")
                print("The correct word was ", word)
                break
            print(guess, " is not in the word")
            print(guesses, " guesses left")
            print("")

playHangman()
