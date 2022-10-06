print("Welcome to Wordle!")
N = 1
while True:
    N += 1
    
    # PLAYER ONE INPUT
    validity = False
    while validity == False:
        playerOneInput = input("Input a five-letter word: ")
        playerWordLetterCount = 0
        
        for char3 in playerOneInput:
            playerWordLetterCount +=1
         
        if playerWordLetterCount != 5:
            print(f'{playerOneInput} is not a five-letter word.')
            continue
       
        validity = True
   
    ########################################################
       
    guessLeft = 6
    gameIndicator = 0
   
    boxesTotalOutput = []

    while guessLeft != 0:
        boxesOutput = []
        list3 = []
        playerTwoInput = input("Guess the five-letter word: ")
        playerTwoWordLetterCount = 0
        stopRepeat = False
        repeatChar = ""
        
        for char5 in playerTwoInput:
            playerTwoWordLetterCount += 1
            if char5 not in list3:
                list3.append(char5)
            else:
                repeatChar = char5

        if playerTwoWordLetterCount != 5:
            print(f'{playerTwoInput} is not a five-letter word.')
            continue
       
        else:
            if playerTwoInput == playerOneInput:
                gameIndicator += 1
                boxesOutput += '🟩' * 5
                print(''.join(boxesOutput))
                break
           
            else:
                guessLeft -= 1
                index = 0
                for char in playerTwoInput:
                    index += 1
                    for char2 in playerOneInput[index - 1]:
                        if char2 == char:
                            boxesOutput += '🟩'
                            continue
                        
                        if char in playerOneInput:
                            if char != repeatChar:
                                boxesOutput += "🟨"
                                
                            else:
                                if stopRepeat == True:
                                    boxesOutput += '🟨'
                                    stopRepeat = True
                                else: 
                                    boxesOutput += "⬜" 
                        else:
                            boxesOutput += "⬜" 
                           
                print(''.join(boxesOutput))
                gameIndicator +=1
        boxesTotalOutput.append(boxesOutput)  
    boxesTotalOutput.append(boxesOutput)  
   
    # OUTPUT
    print('')      
    print(f'Wordle {N} {gameIndicator}/6')
    for items in boxesTotalOutput:
        print(''.join(items))
