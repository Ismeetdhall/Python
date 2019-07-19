# Gussing Your MOOD PROGRAM
import random
print ("Iam a Megical Program Just put your face in front of Camra")
print ("So you are - ")
mood = random.randrange(3)
if mood == 0:
   
    print( """

      
   
      O      O   
                 
                  
      .------.    
     '        '  
             
    
                     #sad """)
elif mood == 1:
        
        print ("""

    
        _     _  
       (o)   (o)    
                     
     \           /  
      '.       .'   
        `'---'`   
       
                  #Happy """)
elif mood ==2:
    
    print ("""
     
       \\\  //            
       O      O     
                     
                       
          __              
      .-'`  `'-.     
                
      
                #Angry """)
else :
    print( "Your Face Can't be Recognised")
print (" - Today.")
input('\npress enter to exit')
