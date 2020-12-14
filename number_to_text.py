
son=input()
if son.isdigit():
    son=int(son)
    if son>0 and son<1000000000000:

        def yuzlar(son,letter,letter_x):
            qoldiq_1=son%10
            son=son//10
            qoldiq_2=son%10
            son=son//10
            qoldiq_3=son%10
            #yuzlik
            if qoldiq_3==1:
                letter+="bir yuz "
            elif qoldiq_3==2:
                letter+="ikki yuz "
            elif qoldiq_3==3:
                letter+="uch yuz "
            elif qoldiq_3==4:
                letter+="to'rt yuz "
            elif qoldiq_3==5:
                letter+="besh yuz "
            elif qoldiq_3==6:
                letter+="olti yuz "
            elif qoldiq_3==7:
                letter+="yetti yuz "
            elif qoldiq_3==8:
                letter+="sakkiz yuz "
            elif qoldiq_3==9:
                letter+="to'qqiz yuz "
        #onlik
            if qoldiq_2==1:
                letter+="o'n "
            elif qoldiq_2==2:
                letter+="yigirma "
            elif qoldiq_2==3:
                letter+="o'ttiz "
            elif qoldiq_2==4:
                letter+="qirq "
            elif qoldiq_2==5:
                letter+="ellik "
            elif qoldiq_2==6:
                letter+="oltmish "
            elif qoldiq_2==7:
                letter+="yetmish "
            elif qoldiq_2==8:
                letter+="sakson "
            elif qoldiq_2==9:
                letter+="to'qson "
            #birlik
            if qoldiq_1==1:
                letter+="bir "
            elif qoldiq_1==2:
                letter+="ikki "
            elif qoldiq_1==3:
                letter+="uch "
            elif qoldiq_1==4:
                letter+="to'rt "
            elif qoldiq_1==5:
                letter+="besh "
            elif qoldiq_1==6:
                letter+="olti "
            elif qoldiq_1==7:
                letter+="yetti "
            elif qoldiq_1==8:
                letter+="sakkiz "
            elif qoldiq_1==9:
                letter+="to'qqiz "
            print(letter,end=letter_x)

        letter=""
        milliard=son//1000000000
        son=son%1000000000
        letter_1="milliard "
        if milliard!=0:
            yuzlar(milliard,letter,letter_1)


        million=son//1000000
        son=son%1000000
        letter_2="million "
        if million!=0:
            yuzlar(million,letter,letter_2)


        ming=son//1000
        son=son%1000
        letter_3="ming "
        yuzlar(ming,letter,letter_3)


        yuz=son%1000
        yuzlar(yuz,letter,"")

print(letter.strip())





