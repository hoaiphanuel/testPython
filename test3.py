import keyboard
a=[]
i=0
while(i<2) :
    try:

        if ((keyboard.is_pressed('s'))or(keyboard.is_pressed('S'))):
            a.append("s")
            keyboard.stop_recording()
            i+=1
        elif keyboard.is_pressed('P') or keyboard.is_pressed('P'):
            a.append("p")
            i+=1
    except:
        pass
print(a)