
x=input("File: ")
f=open(x,'r')
L=f.readlines()
f.close
w = "v2.0 raw\n"
f=open(x+"asm","w")
f.writelines(w)
f.close
w=""
b=1
endline=8
jmpa=0
for L in L:
    if(L[0:3]=="pri"): 
        i=5
        while(L[i]!='"'):
            c=["e",0,str(hex(ord(L[i]))[2:5]),6,0,0]
            ia=0
            w=""
            jmpa=jmpa+6
            while(ia<len(c)):
                w=w+ str(c[ia])+" "
                ia=ia+1
                b=b+1
                if(b>endline):
                    w=w+"\n"
                    b=1
            i=i+1
            f=open(x+"asm","a")
            f.write(w)
            w=""
            f.close
    if(L[0:3]=="nel"): 
        c=["e",0,"d",6,0,0]
        ia=0
        w=""
        jmpa=jmpa+6
        while(ia<len(c)):
            w=w+ str(c[ia])+" "
            ia=ia+1
            b=b+1
            if(b>endline):
                w=w+"\n"
                b=1
        f=open(x+"asm","a")
        f.write(w)
        w=""
        f.close   
    if(L[0:3]=="var"): 
        i=9
        r=L[5]
        d=""
        jmpa=jmpa+3
        while(L[i]!='"'):
            d=d+L[i]
            i=i+1
            ia=0
            c=["e",r,d]
        while(ia<len(c)):
            w=w+ str(c[ia])+" "
            ia=ia+1
            b=b+1
            if(b>endline):
                w=w+"\n"
                b=1
        
        f=open(x+"asm","a")
        f.write(w)
        w=""
        f.close
    if(L[0:3]=="prr"): 
        ia=0
        r=L[5]
        d=L[9]
        c=["7",r,d]
        jmpa=jmpa+3
        while(ia<len(c)):
            w=w+ str(c[ia])+" "
            ia=ia+1
            b=b+1
            if(b>endline):
                w=w+"\n"
                b=1
        f=open(x+"asm","a")
        f.write(w)
        w=""
        f.close
    if(L[0:3]=="out"): 
        ia=0
        r=L[5]
        c=["6",r,0]
        jmpa=jmpa+3
        while(ia<len(c)):
            w=w+ str(c[ia])+" "
            ia=ia+1
            b=b+1
            if(b>endline):
                w=w+"\n"
                b=1
        f=open(x+"asm","a")
        f.write(w)
        w=""
        f.close
    if(L[0:3]=="get"): 
        ia=0
        r=L[5]
        c=["5",r,0]
        jmpa=jmpa+3
        while(ia<len(c)):
            w=w+ str(c[ia])+" "
            ia=ia+1
            b=b+1
            if(b>endline):
                w=w+"\n"
                b=1
        f=open(x+"asm","a")
        f.write(w)
        w=""
        f.close
    if(L[0:3]=="sme"): 
        ia=0
        r=L[5]
        c=["1",r,0]
        jmpa=jmpa+3
        while(ia<len(c)):
            w=w+ str(c[ia])+" "
            ia=ia+1
            b=b+1
            if(b>endline):
                w=w+"\n"
                b=1
        f=open(x+"asm","a")
        f.write(w)
        w=""
        f.close
    if(L[0:3]=="gme"): 
        ia=0
        r=L[5]
        c=["2",r,0]
        jmpa=jmpa+3
        while(ia<len(c)):
            w=w+ str(c[ia])+" "
            ia=ia+1
            b=b+1
            if(b>endline):
                w=w+"\n"
                b=1
        f=open(x+"asm","a")
        f.write(w)
        w=""
        f.close
    if(L[0:3]=="jmp"): 
        ia=0
        r=L[5]
        c=["3",r,0]
        jmpa=jmpa+3
        while(ia<len(c)):
            w=w+ str(c[ia])+" "
            ia=ia+1
            b=b+1
            if(b>endline):
                w=w+"\n"
                b=1
        f=open(x+"asm","a")
        f.write(w)
        w=""
        f.close
    if(L[0:3]=="alu"): 
        ia=0
        c=["4",0,0]
        jmpa=jmpa+3
        while(ia<len(c)):
            w=w+ str(c[ia])+" "
            ia=ia+1
            b=b+1
            if(b>endline):
                w=w+"\n"
                b=1
        f=open(x+"asm","a")
        f.write(w)
        w=""
        f.close
    if(L[0:3]=="com"): 
        ia=0
        c=["b",0,0]
        jmpa=jmpa+3
        while(ia<len(c)):
            w=w+ str(c[ia])+" "
            ia=ia+1
            b=b+1
            if(b>endline):
                w=w+"\n"
                b=1
        f=open(x+"asm","a")
        f.write(w)
        w=""
        f.close
    if(L[0:3]=="wai"): 
        ia=0
        c=["a",0,0]
        jmpa=jmpa+3
        while(ia<len(c)):
            w=w+ str(c[ia])+" "
            ia=ia+1
            b=b+1
            if(b>endline):
                w=w+"\n"
                b=1
        f=open(x+"asm","a")
        f.write(w)
        w=""
        f.close
    if(L[0:3]=="dsc"): 
        ia=0
        r=L[5]
        c=["d",r,0]
        jmpa=jmpa+3
        while(ia<len(c)):
            w=w+ str(c[ia])+" "
            ia=ia+1
            b=b+1
            if(b>endline):
                w=w+"\n"
                b=1
        f=open(x+"asm","a")
        f.write(w)
        w=""
        f.close
    if(L[0:3]=="sav"): 
        ia=0
        c=[8,0,0]
        jmpa=jmpa+1
        while(ia<len(c)):
            w=w+ str(c[ia])+" "
            ia=ia+1
            b=b+1
            if(b>endline):
                w=w+"\n"
                b=1
        f=open(x+"asm","a")
        f.write(w)
        w=""
        f.close
    if(L[0:3]=="dat"): 
        ia=0
        r=L[5]
        a=L[9]
        c=["0",r,a]
        jmpa=jmpa+1
        while(ia<len(c)):
            w=w+ str(c[ia])+" "
            ia=ia+1
            b=b+1
            if(b>endline):
                w=w+"\n"
                b=1
        f=open(x+"asm","a")
        f.write(w)
        w=""
        f.close
    if(L[0:3]=="end"): 
        ia=0

        c=["f","0","0"]
        jmpa=jmpa+1
        while(ia<len(c)):
            w=w+ str(c[ia])+" "
            ia=ia+1
            b=b+1
            if(b>endline):
                w=w+"\n"
                b=1
        f=open(x+"asm","a")
        f.write(w)
        w=""
        f.close






print("Wielkość danych = "+str(jmpa))

