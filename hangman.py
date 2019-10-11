import  random
word_list=["cat","dog","bike","peach","train"]
def hangman(word):
    wrong=0
    stages=["",
            "_______         ",
            "|               ",
            "|      |        ",
            "|      0        ",
            "|     /|\\      ",
            "|     / \\      ",
            "|               "]
    rletters=list(word)
    board=["_"]*len(word)
    win=False
    print("welcom to hanged-man")
    while wrong<len(stages):
        char=input("please input one character")
        if char in rletters:
            cidx=rletters.index(char)
            board[cidx]=char
            rletters[cidx]='$'
        else:
            wrong+=1
        print(" ".join(board))
        print("\n".join(stages[:wrong]))
        if "_" not in board:
            print("you win")
            win=True
            break
    if win==False:
        print("you lose")

hangman(word_list[random.randint(0,len(word_list))])