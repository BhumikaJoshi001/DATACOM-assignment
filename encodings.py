import numpy as np
import matplotlib.pyplot as plt

def plot_signal(time,signal,title="LINE ENCODING SCHEME"):
    plt.figure(figsize=(10,4))
    plt.axhline(0,color="black",linewidth=1.5)#axhline?== axis horizontal line!

    plt.step(time,signal,where="post",linewidth=2)
    plt.title(title)
    plt.xlabel("Time")
    plt.ylabel("Amplitude")
    plt.ylim(-1.5, 1.5)
    plt.grid(True)
    plt.show()

def NRZ_L(bits):
    signal=[]
    time=[]
    prev=0
    for bit in bits:
        if bit=="1":
            level=1
        else:
            level=-1
        time.extend([prev,prev+1])
        signal.extend([level,level])

        prev=prev+1

    return time,signal

def NRZ_I(bits):
    signal=[]       
    time=[]        
    prev=0            
    last_level = -1    #(taki ab phla 1 +positive logic ke accoridng +1 ho jaye (-1)*(-1)==1)

    for bit in bits:
        if bit=='1' or bit==1:    
            last_level=last_level*(-1)       
        time.extend([prev,prev+1])
        signal.extend([last_level,last_level])

        prev=prev+1

    return time,signal

def Manchester(bits):
    signal=[]
    time=[]
    prev=0
    for bit in bits:
        if bit=="1":
            first_half=1
            second_half=-1
        else:
            first_half=-1
            second_half=1
        signal.extend([first_half,second_half,second_half])
        time.extend([prev,prev+0.5,prev+1])#(2 baar second half dene se end tak vahi rhega jese start aur end point dete the bakiyon mein!)
        prev=prev+1
    return time, signal  

def Differential_Manchester(bits):#1 pe same jesa chl rha hai but 0 pe transition!
   signal=[]
   time=[]
   last_level=1
   prev=0
   for bit in bits:
       
        if bit=="0":
            last_level=last_level*-1

        first_half=last_level
        second_half=-last_level  

        signal.extend([first_half,second_half,second_half])
        time.extend([prev,prev+0.5,prev+1])
        
        prev=prev+1
        last_level =second_half#(so that next time same place start (same rahe then we will change it if bit ==0))
   return time,signal 


def AMI(bits):
    signal=[]
    time=[]
    last_polarity=-1#because -1*-1 one ho for the first one jo milega
    prev=0
    for bit in bits:
        if bit=="1" or bit=="B":
            last_polarity=last_polarity*(-1)
            level=last_polarity
        elif(bit=="V"):
            level=last_polarity
            
        else:#(bit agar B nahi hai 1 nahi hai V nahi hai means 0 toh 0 pe toh 0 pe rhta hai !)
            level=0
        signal.extend([level,level])
        time.extend([prev,prev+1])
        prev=prev+1
    return time,signal

def HDB3(bits):
    bits=list(bits)#list mein issilie convert kia takki loop aur slicing vgrh kr paye asani se 
    no_of_Ones=0
    i=0
    while i<len(bits):
        if bits[i:i+4]==['0','0','0','0']:
            if no_of_Ones % 2==0:
                bits[i]="B"
                bits[i+1]="0"
                bits[i+2]="0"
                bits[i+3]="V"
            else:
                bits[i]="0"
                bits[i+1]="0"
                bits[i+2]="0"
                bits[i+3]="V"
            no_of_Ones=0 #(no of ones ko ferse reset )
            i=i+4
        else:
            if bits[i]=="1":
                no_of_Ones=no_of_Ones+1
            i=i+1
    return bits



#jo bitstream mili hai hum usmein hi changes kr rhe hai issilie 0 milega toh kuch nahi kia kyuki agr 4 se kam zero hai toh hum usse aise hi rhnedenge bitsream mein
#hdb3 vala fucntion kewal scrambled input bitstream de rha hai uske baaad vo scrambled bitstream ko mai ami mein paas kr rhi ho so that it generates a plot!


def B8ZS(bits):
    bits=list(bits)
    i=0
    while i<len(bits):
        if bits[i:i+8]==["0","0","0","0","0","0","0","0"]:
            bits[i:i+8]=["0","0","0","V","B","0","V","B"]
            i=i+8
        else:
            i=i+1
    return bits
#(baki 1 aur 0 ko as it is rhendo vo ami plot krlega (kyuki main function mien hum last mein hdb3 aur b8zs ki plotting ami se hi kra rhe hai !)but for long chain of 8 zeroes hum isko scramble kr rhe hai !)



def PCM():
    samples=list(map(float, input("Enter sampled analog values (comma-separated): ").split(',')))

    levels=list(range(-3,5))  

    if any(x<-3 or x>4 for x in samples):
        print("\n Error: Range not defined! Please enter values between -3 and +4 only.")
        return  

    level_to_code = {level: i for i, level in enumerate(levels)}

    print("\nQuantization Levels and Codes:")
    for level, code in level_to_code.items():
        print(f"{level:>2} → {code:03b}")

    quantized=[min(levels,key=lambda L: abs(L - x)) for x in samples]
    print("\nQuantized Values:",quantized)

    binary_codes=[format(level_to_code[q],'03b') for q in quantized]
    print("Binary Codes:", binary_codes)

    bitstream = ''.join(binary_codes)
    print("\nFinal Bitstream:", bitstream)

def Delta_Modulation():
    
    samples =list(map(float,input("Enter sampled (quantized) values (comma-separated): ").split(',')))

    if len(samples)<2:
        print(" ERROR! At least two samples required for Delta Modulation")
        return

    bitstream=[]

    for i in range(1,len(samples)):
        if samples[i]>samples[i-1]:
            bitstream.append('1')  
        else:
            bitstream.append('0')  

    bitstream_str = ''.join(bitstream)

    print("\nInput Samples: ",samples)
    print("Delta Modulation Bitstream: ",bitstream_str)


    #####PLOTTTING USINGGGG ANYY TYPE OF DIGITAL ENCODINGGG !!! SCRAMBLING DONEE!! YEAHHHHHHHH!
    print("\nAvailable Digital Encodings:")
    print("1: NRZ-L")
    print("2: NRZ-I")
    print("3: Manchester")
    print("4: Differential Manchester")
    print("5: AMI")

    choice = input("Enter your choice (1-5): ").strip()
    if choice=="1":
        t,s=NRZ_L(bitstream_str)
        plot_signal(t,s,"NRZ-L encoding")
    elif choice=="2":
        t,s=NRZ_I(bitstream_str)
        plot_signal(t,s,"NRZ-I encoding")
    elif choice=="3":
        t,s=Manchester(bitstream_str)
        plot_signal(t,s,"Manchester encoding")
    elif choice=="4":
        t,s=Differential_Manchester(bitstream_str)
        plot_signal(t,s,"Differential_Manchester encoding")
    elif choice=="5":
        t,s=AMI(bitstream_str)
        scramble=input("Apply Scrambling?? (yes/no) ").strip().lower()
        if scramble=="yes":
            scrambling_type=input("Choose type : (B8ZS/HDB3): ").strip().upper()
            if scrambling_type == "B8ZS":
                scrambled_data = B8ZS(bitstream_str)
            elif scrambling_type == "HDB3":
                scrambled_data = HDB3(bitstream_str)
            else:
                print("INVALID SCRAMBLING TECHNIQUE")
                return

            t, s = AMI(scrambled_data)
            plot_signal(t, s, f"AMI with {scrambling_type} Scrambling")

               
        else:
            plot_signal(t,s,"ami encoding")
    else:
            print("Invalid choice.")
    



    

def main():
    print(" LINE ENCODING VISUALIZER ")

    

    signal_type = input("Enter type (DIGITAL / ANALOG): ").strip().lower()

    if signal_type == "digital":
        data = input("Enter Binary Data (e.g. 10101110): ").strip()
        print("\nAvailable Digital Encodings:")
        print("1: NRZ-L")
        print("2: NRZ-I")
        print("3: Manchester")
        print("4: Differential Manchester")
        print("5: AMI")

        choice = input("Enter your choice (1-5): ").strip()
        if choice=="1":
            t,s=NRZ_L(data)
            plot_signal(t,s,"NRZ-L encoding")
        elif choice=="2":
            t,s=NRZ_I(data)
            plot_signal(t,s,"NRZ-I encoding")
        elif choice=="3":
            t,s=Manchester(data)
            plot_signal(t,s,"Manchester encoding")
        elif choice=="4":
            t,s=Differential_Manchester(data)
            plot_signal(t,s,"Differential_Manchester encoding")
        elif choice=="5":
            t,s=AMI(data)
            scramble=input("Apply Scrambling?? (yes/no) ").strip().lower()
            if scramble=="yes":
                scrambling_type=input("Choose type : (B8ZS/HDB3): ").strip().upper()
                if scrambling_type == "B8ZS":
                    scrambled_data = B8ZS(data)
                elif scrambling_type == "HDB3":
                    scrambled_data = HDB3(data)
                else:
                    print("INVALID SCRAMBLING TECHNIQUE")
                    return

                t, s = AMI(scrambled_data)
                plot_signal(t, s, f"AMI with {scrambling_type} Scrambling")

               
            else:
                plot_signal(t,s,"ami encoding")
        else:
            print("Invalid choice.")

    elif signal_type == "analog":
        print("Available Analog Encodings:")
        print("1. PCM")
        print("2. Delta Modulation")
        choice = input("Enter choice (1 or 2): ").strip()

        if choice == "1":
            PCM() 
        elif choice == "2":
            Delta_Modulation()
        else:
            print("Invalid choice.")

    
    else:
        print("Invalid input type. Please enter DIGITAL or ANALOG.")







    
if __name__ == "__main__":
    main()
