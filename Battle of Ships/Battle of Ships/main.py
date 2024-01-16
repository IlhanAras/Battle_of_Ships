import numpy as np
import sys
from os.path import exists
try:
    file1=sys.argv[1]
    file2=sys.argv[2]
    file3=sys.argv[3]
    file4=sys.argv[4]
    
    flage31=True
    player1gameorder,player1boomlist=[],[]
    player2gameorder,player2boomlist=[],[]
    strforpla,roundcount="",1
    listforpla,listforpc=[],[]
    strforpc,flag2="",True
    index=0
    indexpla=0
    indexpc=0
    fg=True
    coordina=0

    def iswinnerpla1():#a={"a":"x x x x","c":"x x","w":"x x x"}
        global hittedplayer1,hittedpc
        if len(hittedplayer1)==27:
            return True
        
                   
    def iswinnerpc():#a={"a":"x x x x","c":"x x","w":"x x x"}
        global hittedpc
        if len(hittedpc)==27:
            return True
    
    def saving_func(inpt):#save messages into text file
            with open('Battleship.out', "a",encoding="utf-8") as f:
                f.write(inpt)
                f.close()

    def patlat(coordinate):
        global flag2,listforpc,listforpla,playercizgilist,pccizgilist
        global player1gameorder,player2gameorder,roundcount,hittedplayer1
        rowcoor=int(coordinate.split(",")[0])-1
        colcoor=int(ord(coordinate.split(",")[1])-65)
        try:
            if flag2:
                if player2gameorder[rowcoor][colcoor]=="-":
                    pccizgilist[rowcoor][colcoor]="O"
                elif player2gameorder[rowcoor][colcoor]!="-":
                    pccizgilist[rowcoor][colcoor]="X"
                    colcoor=colcoor+1
                    hittedpc.append(colcoor+rowcoor*10)
            else:
                if player1gameorder[rowcoor][colcoor]=="-":
                    playercizgilist[rowcoor][colcoor]="O"
                    
                elif player1gameorder[rowcoor][colcoor]!="-":
                    playercizgilist[rowcoor][colcoor]="X"
                    colcoor=colcoor+1
                    hittedplayer1.append(colcoor+rowcoor*10)

                roundcount+=1

        except:
            print("kaboom:error")
        if iswinnerpc() and iswinnerpla1():
            saving_func("\nDraw\n")
            makingtable(playercizgilist,pccizgilist)
            exit()
        if iswinnerpla1():
            saving_func("\nPlayer2 Wins!\n")
            makingtable(playercizgilist,pccizgilist)
            exit()

        if iswinnerpc():
            print("\nPlayer1 Wins!\n")
            makingtable(playercizgilist,pccizgilist)
            exit()
        makingtable(playercizgilist,pccizgilist)
        
    def boomlistcooncater(pla1boom,pla2boom):
            pla1boom,pla2boom=pla1boom[0],pla2boom[0]
            global flag2,coordina,indexpla,indexpc
            try:
                for i in range(len(pla1boom)+len(pla2boom)+1):
                    
                    if flag2:
                        while len([x for x in pla1boom[indexpla].split(",") if x])<2:
                            #print(len(pla1boom[indexpla]))
                            saving_func(f"\nIndexError: <your message>{pla1boom[indexpla]}\n")
                            indexpla+=1
                        #sayi,harf
                        while (not pla1boom[indexpla].split(",")[0].isdigit()) or (not pla1boom[indexpla].split(",")[1].isalpha()):
                            saving_func(f"\nValueError: <your message>{pla1boom[indexpla]}\n")
                            indexpla+=1
                        
                        while (int(pla1boom[indexpla].split(",")[0])>10) or ord(pla1boom[indexpla].split(",")[1])>74:
                            saving_func(f"\nAssertionError: Invalid Operation{pla1boom[indexpla]}\n")
                            indexpla+=1
                            
                        saving_func(f"Enter your move: {pla1boom[indexpla]}\n")
                        patlat(pla1boom[indexpla])
                        
                        flag2=False
                        indexpla+=1
                               
                    else:
                        
                        while len(pla2boom[indexpc].split(","))!=2:
                            saving_func("\nIndexError: <your message>\n")
                            indexpc+=1
                        else:
                            while (not pla2boom[indexpc].split(",")[0].isdigit()) or (not pla2boom[indexpc].split(",")[1].isalpha()):
                                saving_func("\ValueError: <your message>qwqwqwq\n")
                                indexpc+=1
                            else: 
                                saving_func(f"Enter your move: {pla2boom[indexpc]}\n")
                                patlat(pla2boom[indexpc])  
                                indexpc+=1
                                flag2=True 
            except:
                print("kaboom:error")
    harfler=[chr(x+65) for x in range(10)]
    ilkprintplayerflag=True
    def makingtable(plalist,pclist):
        global strforpc,strforpla,listforpla,listforpc,playercizgilist,pccizgilist,roundcount,flag2,ilkprintplayerflag,index
        global player1boomlist,player2boomlist,coordina,fg,flage31,harfler
        if  iswinnerpc() or  iswinnerpla1():
            saving_func(f"\nFinal Information\n\nPlayer1's Hidden Board\t\tPlayer2's Hidden Board\n")
            strforpla+=" "
            strforpc+=" "
            for letter in harfler:
                strforpla+=f" {letter}"
                strforpc+=f" {letter}"

            strforpla+="\n"
            strforpc+="\n"    
            timer=1   
            for row1,row2 in zip(plalist,pclist):
                strforpla+=f"{timer:<2}"
                strforpc+=f"{timer:<2}"
                timer+=1
                ct3=0
                for let in row1:
                    if ct3==9 :
                        strforpla+=f"{let}"
                    elif let=="C" or let=="P" or let=="S"or let=="D"or let=="B" or let=="O":
                        strforpla+=f"{let} "
                        ct3+=1
                    else: 
                        strforpla+=f"{let} "
                        ct3+=1
                ct4=0
                for let2 in row2:
                    if ct4==9 :
                        strforpc+=f"{let2}"
                    elif let2=="C" or let2=="P" or let2=="S"or let2=="D"or let2=="B" or let2=="O":
                        strforpc+=f"{let2} "
                        ct4+=1        
                    else:
                        strforpc+=f"{let2} "
                        ct4+=1
                strforpla+="\n"
                strforpc+="\n"        

            strforpla+="\n"
            strforpc+="\n" 
            cizgiyapici()
            listforpla=strforpla.split("\n") 
            listforpc=strforpc.split("\n")          
                
            for i in range(len(listforpla)):
                saving_func(f'{str(listforpla[i])}\t\t{listforpc[i]}\n')
                    
            del listforpc,listforpla
            strforpc,strforpla="",""
        else:
            if flage31:
                saving_func(f"Battle of Ships Game\n\n")
                flage31=False
            if ilkprintplayerflag:
                saving_func(f"Player1's move\n\n")
                ilkprintplayerflag=False
            elif flag2 :
                saving_func(f"\nPlayer2's move\n\n")

            else:
                saving_func(f"\nPlayer1's move\n\n")

                #print(f"Player1's move\n")
            saving_func(f"Round : {roundcount:<3}\t\t\t\t\tGrid Size: 10x10\n\n")
            saving_func(f"Player1's Hidden Board\t\tPlayer2's Hidden Board\n")
            strforpla+=" "
            strforpc+=" "
            for letter in harfler:
                strforpla+=f" {letter}"
                strforpc+=f" {letter}"

            strforpla+="\n"
            strforpc+="\n"    
            timer=1   
            for row1,row2 in zip(plalist,pclist):
                strforpla+=f"{timer:<2}"
                strforpc+=f"{timer:<2}"
                timer+=1
                ct=0
                for let in row1:
                    if ct==9 :
                        strforpla+=f"{let}"

                    elif let=="C" or let=="P" or let=="S"or let=="D"or let=="B" or let=="O":
                        strforpla+=f"{let} "
                        ct+=1
                    else: 
                        strforpla+=f"{let} "
                        ct+=1
                #print(ct) 
                ct2=0       
                for let2 in row2:
                    if ct2==9 :
                        strforpc+=f"{let2}"

                    elif let2=="C" or let2=="P" or let2=="S"or let2=="D"or let2=="B" or let2=="O":
                        strforpc+=f"{let2} " 
                        ct2+=1        
                    else:
                        strforpc+=f"{let2} "
                        ct2+=1

                strforpla+="\n"
                strforpc+="\n"        

            strforpla+="\n"
            strforpc+="\n" 
            cizgiyapici()
            listforpla=strforpla.split("\n") 
            listforpc=strforpc.split("\n")          
                
            for i in range(len(listforpla)):
                saving_func(f'{str(listforpla[i])}\t\t{listforpc[i]}\n')
            del listforpc,listforpla
            strforpc,strforpla="",""

    def matrixmaker(liste):
        for i in range(len(liste)):
            for a in range(len(liste[i])):
                if liste[i][a]=="":
                    liste[i][a]="-"
        return(liste)
                                        
    file_to_delete = open("Battleship.out",'w',encoding="utf-8")# opens output file to clearing
    file_to_delete.close() 
    with open(f'{file3}',encoding="utf-8") as f: #file3 
            for line in f.readlines():
                line=line.strip("\n")
                info=line.split(";")
                info.pop()
                player1boomlist.append(info)

    with open(f'{file4}',encoding="utf-8") as f:  #file4
            for line in f.readlines():
                line=line.strip("\n")
                info=line.split(";")
                info.pop()
                player2boomlist.append(info)

    with open(f'{file1}',encoding="utf-8") as f: #file1
            for line in f.readlines():
                line=line.strip("\n")
                player1gameorder.append(line)

    with open(f'{file2}',encoding="utf-8") as f:  #file2
            for line in f.readlines():
                line=line.strip("\n")
                player2gameorder.append(line)    
    
    player1gameorder=list(map(lambda n: n.split(";"),player1gameorder))
    player2gameorder=list(map(lambda n: n.split(";"),player2gameorder))
    player1gameorder=matrixmaker(player1gameorder)
    player2gameorder=matrixmaker(player2gameorder)


    aforpc=np.array(player2gameorder)
    diforpc={"s":[],"c":[],"b":[],"d":[],"p":[]}
    hittedpc=[]
    cizgiforpcgemiler={"c":"-","b":"- -","d":"-","s":"-","p":"- - - -"}
    batangemilerforpc=[]

    aforplayer=np.array(player1gameorder)
    diforplayer={"s":[],"c":[],"b":[],"d":[],"p":[]}
    hittedplayer1=[]
    cizgiforpla1gemiler={"c":"-","b":"- -","d":"-","s":"-","p":"- - - -"}
    batangemilerforpla1=[]


    def gemiakillikordinat():
        global aforplayer,diforplayer,aforpc,diforpc
        for row in range(len(aforplayer)):
            for col in range(len(aforplayer[0])):
                #s boat 3 size
                if  aforplayer[row][col]=="S":
                    if list(aforplayer[row:row+3,col])==list("S"*3):
                        diforplayer["s"].append(tuple(col+1+x*10 for x in range(row,row+3)))
                        aforplayer[row:row+3,col]=[0,0,0]

                    if list(aforplayer[row,col:col+3])==list("S"*3):
                        diforplayer["s"].append(tuple(row*10+x+1 for x in range(col,col+3)))
                        aforplayer[row,col:col+3]=[0,0,0]
                #c boat 5 size
                if  aforplayer[row][col]=="C":
                    if list(aforplayer[row:row+5,col])==list("C"*5):
                        diforplayer["c"].append(tuple(col+1+x*10 for x in range(row,row+5)))
                        aforplayer[row:row+5,col]=[0,0,0,0,0]
                    if list(aforplayer[row,col:col+5])==list("C"*5):
                        diforplayer["c"].append(tuple(row*10+x+1 for x in range(col,col+5)))
                        aforplayer[row,col:col+5]=[0,0,0,0,0]

                #b boat 4 size
                if  aforplayer[row][col]=="B":
                    if list(aforplayer[row:row+4,col])==list("B"*4):
                        diforplayer["b"].append(tuple(col+1+x*10 for x in range(row,row+4)))
                        aforplayer[row:row+4,col]=[0,0,0,0]

                    if list(aforplayer[row,col:col+4])==list("B"*4):
                        diforplayer["b"].append(tuple(row*10+x+1 for x in range(col,col+4)))
                        aforplayer[row,col:col+4]=[0,0,0,0]
                #d boat 3 size
                if  aforplayer[row][col]=="D":
                    if list(aforplayer[row:row+3,col])==list("D"*3):
                        diforplayer["d"].append(tuple(col+1+x*10 for x in range(row,row+3)))
                        aforplayer[row:row+3,col]=[0,0,0]
                    if list(aforplayer[row,col:col+3])==list("D"*3):
                        diforplayer["d"].append(tuple(row*10+x+1 for x in range(col,col+3)))
                        aforplayer[row,col,col+3]=[0,0,0]
                #patrolboat 2 size
                if  aforplayer[row][col]=="P":
                    if list(aforplayer[row:row+2,col])==list("P"*2):
                        diforplayer["p"].append(tuple(col+1+x*10 for x in range(row,row+2)))
                        aforplayer[row:row+2,col]=[0,0]
                    if list(aforplayer[row,col:col+2])==list("P"*2):
                        diforplayer["p"].append(tuple(row*10+x+1 for x in range(col,col+2)))
                        aforplayer[row,col:col+2]=[0,0]

        
        for row in range(len(aforpc)):
            for col in range(len(aforpc[0])):
                #s boat 3 size
                if  aforpc[row][col]=="S":
                    if list(aforpc[row:row+3,col])==list("S"*3):
                        diforpc["s"].append(tuple(col+1+x*10 for x in range(row,row+3)))
                        aforpc[row:row+3,col]=[0,0,0]

                    if list(aforpc[row,col:col+3])==list("S"*3):
                        diforpc["s"].append(tuple(row*10+x+1 for x in range(col,col+3)))
                        aforpc[row,col:col+3]=[0,0,0]
                #c boat 5 size
                if  aforpc[row][col]=="C":
                    if list(aforpc[row:row+5,col])==list("C"*5):
                        diforpc["c"].append(tuple(col+1+x*10 for x in range(row,row+5)))
                        aforpc[row:row+5,col]=[0,0,0,0,0]
                    if list(aforpc[row,col:col+5])==list("C"*5):
                        diforpc["c"].append(tuple(row*10+x+1 for x in range(col,col+5)))
                        aforpc[row,col:col+5]=[0,0,0,0,0]
                #b boat 4 size
                if  aforpc[row][col]=="B":
                    if list(aforpc[row:row+4,col])==list("B"*4):
                        diforpc["b"].append(tuple(col+1+x*10 for x in range(row,row+4)))
                        aforpc[row:row+4,col]=[0,0,0,0]
                    if list(aforpc[row,col:col+4])==list("B"*4):
                        diforpc["b"].append(tuple(row*10+x+1 for x in range(col,col+4)))
                        aforpc[row,col:col+4]=[0,0,0,0]
                #d boat 3 size
                if  aforpc[row][col]=="D":
                    if list(aforpc[row:row+3,col])==list("D"*3):
                        diforpc["d"].append(tuple(col+1+x*10 for x in range(row,row+3)))
                        aforpc[row:row+3,col]=[0,0,0]
                    if list(aforpc[row,col:col+3])==list("D"*3):
                        diforpc["d"].append(tuple(row*10+x+1 for x in range(col,col+3)))
                        aforpc[row,col:col+3]=[0,0,0]
                #patrolboat 2 size
                if  aforpc[row][col]=="P":
                    if list(aforpc[row:row+2,col])==list("P"*2):
                        diforpc["p"].append(tuple(col+1+x*10 for x in range(row,row+2)))
                        aforpc[row:row+2,col]=[0,0]
                    if list(aforpc[row,col:col+2])==list("P"*2):
                        diforpc["p"].append(tuple(row*10+x+1 for x in range(col,col+2)))
                        aforpc[row,col:col+2]=[0,0]

    gemiakillikordinat()
    def cizgiyapici():        
        global cizgiforpla1gemiler,batangemilerforpla1 ,strforpla,hittedplayer1           
        global cizgiforpcgemiler,batangemilerforpc,strforpc,hittedpc
        cizgiforpla1gemiler={"c":"-","b":"- -","d":"-","s":"-","p":"- - - -"}
        cizgiforpcgemiler={"c":"-","b":"- -","d":"-","s":"-","p":"- - - -"}

        for key,valof in diforplayer.items():
            for valofdic in valof:
                bolval=(all([val in hittedplayer1 for val in valofdic]))
                if bolval:
                    #a=a.replace("-","x",1)
                    batangemilerforpla1.append(key)
                    cizgiforpla1gemiler[key]=cizgiforpla1gemiler[key].replace("-","x",1)

        for key,valof in diforpc.items():
            for valofdic in valof:
                bolval=(all([val in hittedpc for val in valofdic]))
                if bolval:
                    #a=a.replace("-","x",1)
                    batangemilerforpc.append(key)
                    cizgiforpcgemiler[key]=cizgiforpcgemiler[key].replace("-","x",1)
                       
        strforpla+=(f"Carrier\t\t{cizgiforpla1gemiler['c']}\t\t\n")
        strforpla+=(f"Battleship\t{cizgiforpla1gemiler['b']}\t\t\n")
        strforpla+=(f"Destroyer\t{cizgiforpla1gemiler['d']}\t\t\n")
        strforpla+=(f"Submarine\t{cizgiforpla1gemiler['s']}\t\t\n")
        strforpla+=(f"Patrol Boat\t{cizgiforpla1gemiler['p']}\t\n")

        strforpc+=(f"Carrier\t\t{cizgiforpcgemiler['c']}\n")
        strforpc+=(f"Battleship\t{cizgiforpcgemiler['b']}\n")
        strforpc+=(f"Destroyer\t{cizgiforpcgemiler['d']}\n")
        strforpc+=(f"Submarine\t{cizgiforpcgemiler['s']}\n")
        strforpc+=(f"Patrol Boat\t{cizgiforpcgemiler['p']}\n")


    playercizgilist=[["-" for col in range(10)]for a in range(10)]
    pccizgilist=[["-" for col in range(10)]for a in range(10)]
    makingtable(playercizgilist,pccizgilist)
    boomlistcooncater(player1boomlist,player2boomlist)
   
except IndexError:
    pass

except IOError:
        file_to_delete = open("output.txt",'w',encoding="utf-8")# opens output file to clearing
        file_to_delete.close() 
        fileerrorlist=[]
        if not exists(f"{file4}"):
            fileerrorlist.append(f"{file4}")

        if not exists(f"{file3}"):
            fileerrorlist.append(f"{file3}")

        if not exists(f"{file2}"):
            fileerrorlist.append(f"{file2}")

        if not exists(f"{file1}"):
            fileerrorlist.append(f"{file1}")

        if len(fileerrorlist)==1:
            saving_func(f"IOError: inputfile {fileerrorlist[0]} is not reachable.")  
            print(f"IOError: inputfile {fileerrorlist[0]} is not reachable.") 
        elif len(fileerrorlist)>1:
            toplama=", ".join(fileerrorlist)
            saving_func(f"IOError: inputfiles {toplama} are not reachable.") 
            print(f"IOError: inputfiles {toplama} are not reachable.")

