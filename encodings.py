import numpy as np
import matplotlib.pyplot as plt

def plot_signal(time,signal,title="LINE ENCODING SCHEME"):
    plt.figure(figsize=(8,3))
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
    last_level = 1    

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
        if bit=="1":
            last_polarity=last_polarity*(-1)
            level=last_polarity
        else:
            level=0
        signal.extend([level,level])
        time.extend([prev,prev+1])
        prev=prev+1
    return time,signal


# def PCM():
#     samples=list(map(float,input("Enter sampled values(comma-separated):(MAX LEVELS=8)").split(',')))

# #SABSE PHLE USER INPUT LIA OF THE SAMPLED SIGNAL
#     quantized=[round(x) for x in samples]
#     print("\nQuantized values:",quantized)
# #ROUND FUNCTION KI HELP SE QUANTIZE KIA VALUES KO HUMARE CASE MEIN(4.5 IS ROUNDED OFF TO 4)!

#     max_val=max(quantized)#[JO QUANTIZE KRKE VALUES AAYI LIKE 3,4,2,5 UNMEIN SE SABSE MAX VALI VALUE NIKALI TAKI UTNI HI BITS RKHE HAR KISI KE LIE]
#     bits_per_sample=len(format(max_val,'b'))#YE FUNCTION USS MAXVALUE KO BINARY MEIN CONVERT KREGA AUR USKI LENGTH NIKALEGA SO IT BECOMES BITS PER SAMPLE

#     binary_codes = [format(q, f'0{bits_per_sample}b') for q in quantized]# HAR QUANTIZED VALUE KO BINARY MEIN CONVERT KRO AUR AGAR LENGTH KAM HAI TOH BITS PER SAMPLE KE ACCORDING 0s KI PADDING KRDO
#     print("Binary codes per sample:",binary_codes)

#     bitstream = ''.join(binary_codes)
#     print("Complete bitstream:",bitstream)

#     t,s =NRZ_L(bitstream)

#     plot_signal(t,s,"PCM Encoding using NRZ-L")


def PCM():
    # Step 1: Input samples
    samples = list(map(float, input("Enter sampled analog values (comma-separated): ").split(',')))

    # Step 2: Quantization range
    levels = list(range(-3, 5))  # -3 to +4

    # Step 3: Range check
    if any(x < -3 or x > 4 for x in samples):
        print("\n❌ Error: Range not defined! Please enter values between -3 and +4 only.")
        return  # Stop execution

    # Step 4: Custom mapping (-3→0, -2→1, ..., 4→7)
    level_to_code = {level: i for i, level in enumerate(levels)}

    print("\nQuantization Levels and Codes:")
    for level, code in level_to_code.items():
        print(f"{level:>2} → {code:03b}")

    # Step 5: Quantize each sample to nearest level
    quantized = [min(levels, key=lambda L: abs(L - x)) for x in samples]
    print("\nQuantized Values:", quantized)

    # Step 6: Get corresponding binary codes
    binary_codes = [format(level_to_code[q], '03b') for q in quantized]
    print("Binary Codes:", binary_codes)

    # Step 7: Combine into bitstream
    bitstream = ''.join(binary_codes)
    print("\nFinal Bitstream:", bitstream)

    # Step 8: NRZ-L encoding and plotting
    print("\nAvailable Digital Encodings:")
    print("1: NRZ-L")
    print("2: NRZ-I")
    print("3: Manchester")
    print("4: Differential Manchester")
    print("5: AMI")

    choice = input("Enter your choice (1-5): ").strip()
    if choice=="1":
        t,s=NRZ_L(bitstream)
        plot_signal(t,s,"NRZ-L encoding")
    elif choice=="2":
        t,s=NRZ_I(bitstream)
        plot_signal(t,s,"NRZ-I encoding")
    elif choice=="3":
        t,s=Manchester(bitstream)
        plot_signal(t,s,"Manchester encoding")
    elif choice=="4":
        t,s=Differential_Manchester(bitstream)
        plot_signal(t,s,"Differential_Manchester encoding")
    elif choice=="5":
            t,s=AMI(bitstream)
            plot_signal(t,s,"ami encoding")

# Run the function
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
            PCM()  # already plots using NRZ-L
        elif choice == "2":
            Delta_Modulation()
        else:
            print("Invalid choice.")

    
    else:
        print("Invalid input type. Please enter DIGITAL or ANALOG.")







    
if __name__ == "__main__":
    main()
