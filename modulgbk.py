import random

def play():
    play_again = "y"
    score = 0
    denominator = 0
    
    while play_again == "y":
    
        breaker = False
        while breaker == False:
            print("Nilai kamu " + str(score) + " sedangkan nilai komputer " + str(denominator))
            player = input("Gunting, Batu, Kertas! (g, b, k): ")
            computer = random.choice(["g", "b", "k"])
            
            if player == computer:
                print('Komputer memilih' ,computer)
                print("Yah seri, mulai lagi!")
                print('=======================================================')
                break
            elif (player == "g" and computer == "k") or (player == "b" and computer == "g") or (player == "k" and computer == "b"):
                score += 1
                print('Komputer memilih' ,computer)
                print("Yey kamu menang!")
                print('=======================================================')
                breaker = True
            elif (player == "g" and computer == "b") or (player == "k" and computer == "g") or (player == "b" and computer == "k"):
                denominator += 1
                print('Komputer memilih' ,computer)
                print("Yah kalah...")
                print('=======================================================')
                breaker = True
            else:
                print("Tulis yang bener dodol")
                print('=======================================================')
                break
                
            play_again=input('Mau main gunting, kertas, batu lagi?(y/n): ')
            print('=======================================================')
            
