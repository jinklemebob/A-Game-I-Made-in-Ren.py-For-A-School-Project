# This is the main script that executes the entirety of the game, I thought I'd share it lmao

label splashscreen:
    play music "audio/menum.ogg" 
    scene white

    
    with fade
    pause 1.0 
    show text "Welcome." with dissolve 
    pause 2.0

    show text "Enjoy this experience." with dissolve
    pause 3.5
    hide text with dissolve 
    with dissolve 
    

return



    

transform live:
    xalign 0.0



define e = Character("Aiko")
define d = Character("Natsumi" )
define r = Character("Rin")
define t = Character("You")

image black:
    "images/black-screen.png"

image Aiko:
    "images/Aiko/Aiko_SummerSera_Smile.png"
    zoom 0.3

image AikoDef:
    "images/Aiko/Aiko_SummerSera_Smile.png"
    zoom 0.25
    xalign 0.5
    yalign 2.0
 
image Aiko1:
    "images/Aiko/Aiko_SummerSera_Closed_Open_Blush.png"
    zoom 0.3
    

image Natsumi:
    "images/Natsumi/Natsumi_SummerUni_Closed_Frown.png"

image NatsumiDef:
    "images/Natsumi/Natsumi_SummerUni_Closed_Frown.png"
    zoom 0.75
    xalign 0.5
    yalign -0.5


image Natsumi1:
    "images/Natsumi/Natsumi_SummerUni_Closed_Open_Blush.png"


image Rin:
    "images/Rin/Rin_SummerUni_Smile.png"

image Rin1:
    "images/Rin/Rin_SummerUni_Frown_ClosedEyes_Blush.png"

image movie1 = Movie(size=(1920, 1080), xpos=0, ypos=0, xanchor=0, yanchor=0)
image movie2 = Movie(size=(1920, 1080), xpos=0, ypos=0, xanchor=0, yanchor=0)

define Fade = Fade(0.5, 1.0, 0.5)

screen Starto:
    frame:
        xpadding 40
        ypadding 20
        xalign 0.5
        yalign 0 
        text "Choose a character."
        
    

    imagebutton:
        xpos 30
        ypos 100
        idle "Aiko"
        hover "Aiko1"
        action Jump("AikoPlay")
        hover_sound "audio/GUI/hover.ogg"
        

    imagebutton:
        xpos 600
        ypos 100
        idle "Natsumi"
        hover "Natsumi1"
        action Jump("NatsumiPlay")
        hover_sound "audio/GUI/hover.ogg"
    
    imagebutton:
        xalign 0.9
        ypos 120
        idle "Rin"
        hover "Rin1"
        action Jump("RinPlay")
        hover_sound "audio/GUI/hover.ogg"



    
label start:
    stop music
    with fade 
    pause 1.0

 
    show white with dissolve
    pause 1.0
    show text "Goodluck." with dissolve
    pause 3.0


    
  

    scene black 
    play movie "images/videoplayback.webm"
    show movie1 with dissolve

    with dissolve 
    pause 1.0

    call screen Starto with dissolve 
    
    
label AikoPlay:
  
    show AikoDef
    e "Are you ready?"

    menu:
        "Yes":
            t "Lez do it."
    e "Let's do our best then!"

    window hide 
    hide AikoDef with dissolve
    pause 2.0
    jump AikoMain


label AikoMain:
    stop movie
    scene bg room
    pause 1.0
    show AikoDef with dissolve
    pause 0.5


    "You have [HP] HP remaining."
    e "Get ready."
    


    
    menu:#1
       
    
        e "What does HTML stand for?"

        "Hyped Text Markup Language":
            
            $ HP -= 1
            e "Sorry you're wrong"
            jump check_lives11

 
        "Hyper Text Marked Up Language":
            
            $ HP -= 1
            e "Nope thats not it."
            jump check_lives11
            
            
        "Hyper Text Markup Language":
           
            e "Correct!"
            jump check_lives11
            


    
    
label check_lives11:


    if HP <= 0 :
        jump AikoLose
    else:       
        jump menu22
        

label menu22:
    "You have [HP] HP remaining."
    e "Next question."



    menu:#2        
        e "What does CSS stand for?"


        "Hyped Text Markup Language": 
            
            $ HP -= 1
            e "Sorry you're wrong"
            jump check_lives22
            
            
        "Hyper Text Marked Up Language":
            
            
            $ HP -= 1
            e "Nope thats not it."
            jump check_lives22
            
        "Hyper Text Markup Language":

            e "Correct!"
            jump menu33
        
label check_lives22:


    if HP <= 0 :
        jump AikoLose
    else:       
        jump menu33
        

label menu33:

    "You have [HP] HP remaining."
    e "Get ready."

    
    menu:
       
    
        e "What does HTML stand for?"

        "Hyped Text Markup Language":
            
            $ HP -= 1
            e "Sorry you're wrong"
            jump check_lives33

 
        "Hyper Text Marked Up Language":
            
            $ HP -= 1
            e "Nope thats not it."
            jump check_lives33
            
            
        "Hyper Text Markup Language":
           
            e "Correct!"
            jump menu44
            


    
    
label check_lives33:


    if HP <= 0 :
        jump AikoLose
    else:       
        jump menu44
        

label menu44:
    "You have [HP] HP remaining."
    e "Next question."

    menu: 
        e "What is the closest planet to the sun?"


        "Jupiter": 
            
            $ HP -= 1
            e "Sorry you're wrong"
            jump check_lives44
            
            
        "Mars":
            
            
            $ HP -= 1
            e "Nope thats not it."
            jump check_lives44
            
        "Mercury":

            e "Correct!"
            jump menu55

label check_lives44:


    if HP <= 0 :
        jump AikoLose
    else:       
        jump menu55
   
label menu55:

    "You have [HP] HP remaining."
    e "Get ready."

    
    menu:#1
       
    
        e "What does HTML stand for?"

        "Hyped Text Markup Language":
            
            $ HP -= 1
            e "Sorry you're wrong"
            jump check_lives55

 
        "Hyper Text Marked Up Language":
            
            $ HP -= 1
            e "Nope thats not it."
            jump check_lives55
            
            
        "Hyper Text Markup Language":
           
            e "Correct!"
            jump menu66
            


    
    
label check_lives55:


    if HP <= 0 :
        jump AikoLose
    else:       
        jump menu66
        

label menu66:
    "You have [HP] HP remaining."
    e "Next question."



    menu:#2        
        e "What's your moms number?"


        "Hyped Text Markup Language": 
            
            $ HP -= 1
            e "Sorry you're wrong"
            jump check_lives66
            
            
        "Hyper Text Marked Up Language":
            
            
            $ HP -= 1
            e "Nope thats not it."
            jump check_lives66
            
        "Hyper Text Markup Language":

            e "Correct!"
            jump menu77
        
label check_lives66:


    if HP <= 0 :
        jump AikoLose
    else:       
        jump menu77
        

label menu77:

    "You have [HP] HP remaining."
    e "Get ready."

    
    menu:
       
    
        e "What does HTML stand for?"

        "Hyped Text Markup Language":
            
            $ HP -= 1
            e "Sorry you're wrong"
            jump check_lives77

 
        "Hyper Text Marked Up Language":
            
            $ HP -= 1
            e "Nope thats not it."
            jump check_lives77
            
            
        "Hyper Text Markup Language":
           
            e "Correct!"
            jump menu88
            


    
    
label check_lives77:


    if HP <= 0 :
        jump AikoLose
    else:       
        jump menu88
        

label menu88:
    "You have [HP] HP remaining."
    e "Next question."

    menu: 
        e "What's your moms number?"


        "Hyped Text Markup Language": 
            
            $ HP -= 1
            e "Sorry you're wrong"
            jump check_lives88
            
            
        "Hyper Text Marked Up Language":
            
            
            $ HP -= 1
            e "Nope thats not it."
            jump check_lives88
            
        "Hyper Text Markup Language":

            e "Correct!"
            jump menu99

label check_lives88:


    if HP <= 0 :
        jump AikoLose
    else:       
        jump menu99

label menu99:
    "You have [HP] HP remaining."
    e "Next question."

    menu: 
        e "What's your moms number?"


        "Hyped Text Markup Language": 
            
            $ HP -= 1
            e "Sorry you're wrong"
            jump check_lives99
            
            
        "Hyper Text Marked Up Language":
            
            
            $ HP -= 1
            e "Nope thats not it."
            jump check_lives99
            
        "Hyper Text Markup Language":

            e "Correct!"
            jump menu100

label check_lives99:


    if HP <= 0 :
        jump AikoLose
    else:       
        jump menu100


label menu100:
    "You have [HP] HP remaining."
    e "Next question."

    menu: 
        e "What's your moms number?"


        "Hyped Text Markup Language": 
            
            $ HP -= 1
            e "Sorry you're wrong"
            jump check_lives100
            
            
        "Hyper Text Marked Up Language":
            
            
            $ HP -= 1
            e "Nope thats not it."
            jump check_lives100
            
        "Hyper Text Markup Language":

            e "Correct!"
            jump AikoWin


label check_lives100:


    if HP <= 0 :
        jump AikoLose
    else:       
        jump AikoWin
label AikoLose:
    e "Aww you have no more HP."
    e "That's too bad."
    e "I was supposed to show you something..."
    pause 2.0
    e "{i} fun...{/i}"

    return


label NatsumiPlay:
    
    show NatsumiDef 
    d "I won't hold back okay?"

    menu:
        "You'll lose either way":
            t "You'll lose either way."
            d "Oh, okay :("
            d "{i}That actually hurt me. {/i}"
            d "{i}It looks like I won't have to go easy on him.{/i}"
            d "Goodluck then."
            window hide
            hide NatsumiDef with dissolve
            pause 2.0
            jump NatsumiMain

        "Do your worst":
            t "Do your worst."
            d "What?"
            t "I said what I said"
            d "{i}He really just said that.{/i}"
            d "{i}So be it. </3.{/i}"
            d "Goodluck then."
            window hide
            hide NatsumiDef with dissolve
            pause 2.0
            jump NatsumiMain

        "Goodluck <3":
            t "Best of luck either way."
            d "Okay :3, goodluck!"
            d "{i}I don't care about winning or losing. {/i}"
            d "{i}I must... {/i}"
            d "{i} Confess...{/i}"
            window hide 
            hide NatsumiDef with dissolve
            pause 2.0
            jump NatsumiMain
            
            
            



init:
    $ HP = 3

label NatsumiMain:

    stop movie
    scene bg room
    pause 1.0
    show NatsumiDef with dissolve
    pause 0.5


    "You have [HP] HP remaining."
    d "Get ready."
    


    
    menu:#1
       
    
        d "What does HTML stand for?"

        "Hyped Text Markup Language":
            
            $ HP -= 1
            d "Sorry you're wrong"
            jump check_lives

 
        "Hyper Text Marked Up Language":
            
            $ HP -= 1
            d "Nope thats not it."
            jump check_lives
            
            
        "Hyper Text Markup Language":
           
            d "Correct!"
            jump check_lives 
            


    
    
label check_lives:


    if HP <= 0 :
        jump NatsumiLose
    else:       
        jump menu2
        

label menu2:
    "You have [HP] HP remaining."
    d "Next question."



    menu:#2        
        d "What's your moms number?"


        "Hyped Text Markup Language": 
            
            $ HP -= 1
            d "Sorry you're wrong"
            jump check_lives1
            
            
        "Hyper Text Marked Up Language":
            
            
            $ HP -= 1
            d "Nope thats not it."
            jump check_lives1
            
        "Hyper Text Markup Language":

            d "Correct!"
            jump menu3
        
label check_lives1:


    if HP <= 0 :
        jump NatsumiLose
    else:       
        jump menu3
        

label menu3:

    "You have [HP] HP remaining."
    d "Get ready."

    
    menu:
       
    
        d "What does HTML stand for?"

        "Hyped Text Markup Language":
            
            $ HP -= 1
            d "Sorry you're wrong"
            jump check_lives2

 
        "Hyper Text Marked Up Language":
            
            $ HP -= 1
            d "Nope thats not it."
            jump check_lives2
            
            
        "Hyper Text Markup Language":
           
            d "Correct!"
            jump menu4
            


    
    
label check_lives2:


    if HP <= 0 :
        jump NatsumiLose
    else:       
        jump menu4
        

label menu4:
    "You have [HP] HP remaining."
    d "Next question."

    menu: 
        d "What's your moms number?"


        "Hyped Text Markup Language": 
            
            $ HP -= 1
            d "Sorry you're wrong"
            jump check_lives3
            
            
        "Hyper Text Marked Up Language":
            
            
            $ HP -= 1
            d "Nope thats not it."
            jump check_lives3
            
        "Hyper Text Markup Language":

            d "Correct!"
            jump menu5

label check_lives3:


    if HP <= 0 :
        jump NatsumiLose
    else:       
        jump menu5
   
label menu5:

    "You have [HP] HP remaining."
    d "Get ready."

    
    menu:#1
       
    
        d "What does HTML stand for?"

        "Hyped Text Markup Language":
            
            $ HP -= 1
            d "Sorry you're wrong"
            jump check_lives4

 
        "Hyper Text Marked Up Language":
            
            $ HP -= 1
            d "Nope thats not it."
            jump check_lives4
            
            
        "Hyper Text Markup Language":
           
            d "Correct!"
            jump menu6
            


    
    
label check_lives4:


    if HP <= 0 :
        jump NatsumiLose
    else:       
        jump menu6
        

label menu6:
    "You have [HP] HP remaining."
    d "Next question."



    menu:#2        
        d "What's your moms number?"


        "Hyped Text Markup Language": 
            
            $ HP -= 1
            d "Sorry you're wrong"
            jump check_lives5
            
            
        "Hyper Text Marked Up Language":
            
            
            $ HP -= 1
            d "Nope thats not it."
            jump check_lives5
            
        "Hyper Text Markup Language":

            d "Correct!"
            jump menu7
        
label check_lives5:


    if HP <= 0 :
        jump NatsumiLose
    else:       
        jump menu7
        

label menu7:

    "You have [HP] HP remaining."
    d "Get ready."

    
    menu:
       
    
        d "What does HTML stand for?"

        "Hyped Text Markup Language":
            
            $ HP -= 1
            d "Sorry you're wrong"
            jump check_lives6

 
        "Hyper Text Marked Up Language":
            
            $ HP -= 1
            d "Nope thats not it."
            jump check_lives6
            
            
        "Hyper Text Markup Language":
           
            d "Correct!"
            jump menu8
            


    
    
label check_lives6:


    if HP <= 0 :
        jump NatsumiLose
    else:       
        jump menu8
        

label menu8:
    "You have [HP] HP remaining."
    d "Next question."

    menu: 
        d "What's your moms number?"


        "Hyped Text Markup Language": 
            
            $ HP -= 1
            d "Sorry you're wrong"
            jump check_lives7
            
            
        "Hyper Text Marked Up Language":
            
            
            $ HP -= 1
            d "Nope thats not it."
            jump check_lives7
            
        "Hyper Text Markup Language":

            d "Correct!"
            jump menu9

label check_lives7:


    if HP <= 0 :
        jump NatsumiLose
    else:       
        jump menu10

label menu9:
    "You have [HP] HP remaining."
    d "Next question."

    menu: 
        d "What's your moms number?"


        "Hyped Text Markup Language": 
            
            $ HP -= 1
            d "Sorry you're wrong"
            jump check_lives8
            
            
        "Hyper Text Marked Up Language":
            
            
            $ HP -= 1
            d "Nope thats not it."
            jump check_lives8
            
        "Hyper Text Markup Language":

            d "Correct!"
            jump menu10

label check_lives8:


    if HP <= 0 :
        jump NatsumiLose
    else:       
        jump menu10


label menu10:
    "You have [HP] HP remaining."
    d "Next question."

    menu: 
        d "What's your moms number?"


        "Hyped Text Markup Language": 
            
            $ HP -= 1
            d "Sorry you're wrong"
            jump check_lives9
            
            
        "Hyper Text Marked Up Language":
            
            
            $ HP -= 1
            d "Nope thats not it."
            jump check_lives9
            
        "Hyper Text Markup Language":

            d "Correct!"
            jump NatsumiWin
label check_lives9:


    if HP <= 0 :
        jump NatsumiLose
    else:       
        jump NatsumiWin



label NatsumiLose:
    d "You're out of HP!"  
    d "You could've seen something from me."
    d "But better luck next time."
    d "Feel free to try me again ;)"

    return

label NatsumiWin:
    d "Wow you actually pulled it through."
    d "Congratulations!"
    d "As for your reward, I need you to close your eyes."
    hide NatsumiDef
    scene black
    "Natsumi steps closer, as you close your eyes."



label RinPlay:
    show Rin1
    r "You ready?"

    menu:
        "Yeah.":
            t "Yeah."
            r "Okay, goodluck!"
            window hide
            hide Rin1 with dissolve
            pause 2.0
            jump RinMain

        "Let's get this over with already.":
            t "Let's make this quick okay?"
            r "Uhm okay then."
            r "Goodluck <3"
            window hide
            hide Rin1 with dissolve
            pause 2.0
            jump RinMain
            
            





label RinMain:
    stop movie
    scene bg room 
    pause 1.0
    with dissolve 
    show Rin1 with dissolve
    pause 0.5

   
  
   
    

    
  

           
    




    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.



 
    # This ends the game.

return
