import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import random 
for i in range (5):
    random .randint (1,7)
    senario=random .randint (1,7)
    weretoshoot=["1","2","3"]
    (input("type the number of the qudrent you want to shoot at then press enter. [1_2_3] "))
    print (weretoshoot)              
    if senario==1:
        print ("the keeper saved it!")
    elif senario==5:
        print ("you hit the crossbar!")
    elif senario==6:
        print ("you missed the goal!")
    else:
        print ("you smash it in!!!")





    save=random .randint (1,7)
    thenet=["1","2","3"]
    theside=random .randint (1,3)
    if theside==1:
        leftimages=['taking-penalties.jpg',"istockphoto-505988052-612x612.jpg","20170801-The18-Image-Ronaldo-PK.jpeg"]
        img = mpimg.imread (random.choice(leftimages))
        plt.imshow(img)
        plt.axis('off')  # Hides axes
        plt.show()
        x=int(input("type a number 1-3 on the goal for the place you want to dive to then press enter [1_2_3]"))
        thenet[int (x)-1]="🧤"
        if x==theside: 
            print ("you saved it yay!")        
        elif save==7:
            print ("the ball flew over the ball and hit a bird yay!")
        elif save==6:
            print("the ball hit the bar yay!")
        else:
            print ("he scored awww")
        thenet[0]="⚽"
        print (thenet)
    if theside==2:
        middleimages=['Nenzema-panelka.jpg',"c01ef789952be0cbdb6bd66ce1f09834.jpg","51_1540x.webp"]
        img = mpimg.imread(random.choice(middleimages))
        plt.imshow(img)
        plt.axis('off')  # Hides axes
        plt.show()
        x=int(input("type a number 1-3 on the goal for the place you want to dive to then press enter [1_2_3]"))
        thenet[int (x)-1]="🧤"
        if x==theside: 
            print ("you saved it yay!")        
        elif save==7:
            print ("the ball flew over the ball and hit a bird yay!")
        elif save==6:
            print("the ball hit the bar yay!")
        else:
            print ("he scored awww")
            thenet[1]="⚽"
        print (thenet)
    if theside==3:
        img = mpimg.imread("image.jpg")
        plt.imshow(img)
        plt.axis('off')  # Hides axes
        plt.show()
        x=int(input("type a number 1-3 on the goal for the place you want to dive to then press enter [1_2_3]"))
        thenet[int (x)-1]="🧤"
        if x==theside: 
            print ("you saved it yay!")        
        elif save==7:
            print ("the ball flew over the ball and hit a bird yay!")
        elif save==6:
            print("the ball hit the bar yay!")
        else:
            print ("he scored awww")
            thenet[2]="⚽"
        print (thenet)