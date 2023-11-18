print("please choose the command")
print(">help")
print(">about program")
started=False
stopped=False
choose=input(">").lower()
while choose=="help" or choose=="about program":
    if choose=="about program":
        print("car_engine simulator")
        print("written by amirjaz")
        print(">help")
        print(">about program")
        choose=input(">").lower()
        
    elif choose=="help":
        print("choose the command")
        print(">start")
        print(">stop")
        print(">quit")
        choose_2=input(">").lower()
        if choose_2!="start" and choose_2!="stop" and choose_2!="quit":
            print("wrong command!")
            break
        elif choose_2=="start":
            print("car started...ready to go!")
            if not started:
                print("the engine already started!")
            else:
                started=True

                
                    
    
    
    

            
        elif choose_2=="stop":
            print("car stopped.")
            if not stopped:
                print("the engine already stopped!")
            else:
             stopped=True
            
        elif choose_2=="quit":
            break



        

    
else:
    print("wrong command!")
    