option=int(input('Hamming Code Oluşturmak İçin:1  \nHamming Code da Hata Bulmak İçin:2\n\t Seçiminizi Giriniz:--\n'))

if(option==1):  # HAMMING CODE OLUŞTURULUYOR
    print('Veri Biti: ')
    d=input()
    data=list(d)
    data.reverse()
    c,ch,j,r,h=0,0,0,0,[]

    while ((len(d)+r+1)>(pow(2,r))): #Fazla bitlerin (parity bit) hesaplanması
        r=r+1

    for i in range(0,(r+len(data))):
        p=(2**c)

        if(p==(i+1)):
            h.append(0)
            c=c+1

        else:
            h.append(int(data[j]))
            j=j+1

    for parity in range(0,(len(h))):
        ph=(2**ch)
        if(ph==(parity+1)):
            startIndex=ph-1
            i=startIndex
            toXor=[]

            while(i<len(h)):
                block=h[i:i+ph]
                toXor.extend(block)
                i+=2*ph

            for z in range(1,len(toXor)):
                h[startIndex]=h[startIndex]^toXor[z]
            ch+=1

    h.reverse()
    print('Oluşturulan Hamming Code:- ', end="")
    print(int(''.join(map(str, h))))


elif(option==2): # HAMMING CODE'DA HATA TESPİTİ
    print('Hamming Code-unu Giriniz:')
    d=input()
    data=list(d)
    data.reverse()
    c,ch,j,r,error,h,parity_list,h_copy=0,0,0,0,0,[],[],[]

    for k in range(0,len(data)): #Parity bit sayısının hesaplanması
        p=(2**c)
        h.append(int(data[k]))
        h_copy.append(data[k])
        if(p==(k+1)):
            c=c+1
            
    for parity in range(0,(len(h))): #Parity bitlerin konumları
        ph=(2**ch)
        if(ph==(parity+1)):

            startIndex=ph-1
            i=startIndex
            toXor=[]

            while(i<len(h)):
                block=h[i:i+ph]
                toXor.extend(block)
                i+=2*ph

            for z in range(1,len(toXor)):
                h[startIndex]=h[startIndex]^toXor[z]
            parity_list.append(h[parity])
            ch+=1
    parity_list.reverse() #Parity kontrolü
    error=sum(int(parity_list) * (2 ** i) for i, parity_list in enumerate(parity_list[::-1]))
    
    if((error)==0):
        print('Girilen Hamming Code-da Hata Bulunmamıştır' )

    elif((error)>=len(h_copy)):
        print('Hata Algılanmıyor!')

    else: #Hatanın tespiti ve düzeltilmesi 
        print('Hata',error,'biti')

        if(h_copy[error-1]=='0'):
            h_copy[error-1]='1'

        elif(h_copy[error-1]=='1'):
            h_copy[error-1]='0'
            print('Hata Onarıldıktan Sonra Hamming Code:- ')
        h_copy.reverse()
        print(int(''.join(map(str, h_copy))))

else:
    print('Öyle Bir Seçenek Bulunmamaktadır.')
