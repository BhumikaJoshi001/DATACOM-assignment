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
    """
    NRZ-Inverted (NRZ-I) Encoding:
    - Bit '1'  → toggle the signal (invert the previous level)
    - Bit '0'  → keep the same level
    """

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


def main():
    print(" LINE ENCODING VISUALIZER ")

    data = input("Enter Binary Data (e.g. 10101110): ").strip()

    signal_type = input("Enter type (DIGITAL / ANALOG): ").strip().lower()

    if signal_type == "digital":
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
        # elif choice=="3":
        #     t,s=Manchester(data)
        #     plot_signal(t,s,"Manchester encoding")
        # elif choice=="4":
        #     t,s=Differential_Manchester(data)
        #     plot_signal(t,s,"Differential_Manchester encoding")
        # elif choice=="5":
        #     t,s=AMI(data)
        #     scramble=input("Apply Scrambling?? (yes/no) ").strip().lower()
        #     if scramble=="yes":
        #         scrambling_type=input("Choose type : (B8ZS/HDB3): ").strip.upper()
        #         if scrambling_type=="B8ZS":
        #             data=B8ZS(data)
        #         elif scrambling_type=="HDB3":
        #             data=HDB3(data)
        #         plot_signal(t, s, "AMI Encoding")
        else:
            print("Invalid choice.")

    # elif signal_type=="analog":
    #     print("Available Analog Encodingss:")
    #     print("1. PCM")
    #     print("2. Delta Modulation")
    #     choice=input("enter choice (1 or 2):").strip()
    #     if choice==1:
    #         t,s=PCM(data)
    #         plot_signal(t,s,"PCM Encoding")
    #     elif choice==2:
    #         t,s=Delta_Modulation(data)
    #         plot_signal(t,s,"Delta Modulation")
    #     else:
    #         print("Invalid choice")
    
    else:
        print("Invalid input type. Please enter DIGITAL or ANALOG.")







    
if __name__ == "__main__":
    main()
