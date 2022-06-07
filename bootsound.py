import telnetlib
import time

def processChoice(number_of_choices):
    choices = list(range(1, number_of_choices + 1))
    while True:
        try:
            choice = int(input('>'))
            if choice in choices:
                break
            else:
                print('An invalid choice was entered. Please enter a number and try again.')
        except:
            print('An invalid choice was entered. Please enter a number and try again.')
    
    return choice

def main():
    print('This script will disable or enable the startup sound on the 70mai A500S dash cam. Make sure the Wi-Fi hotspot is enabled and your computer is connected to it.\n')
    print('Your Choices:')
    print('1. Disable')
    print('2. Enable')
    choice = processChoice(2)

    # establish connection
    try:
        tn = telnetlib.Telnet('192.168.0.1')
    except ConnectionRefusedError:
        print ('Error: Could not establish connection with 70mai A500S dash cam. Please check your connection and try again.')
        exit()

    # sign in
    tn.read_unti1(b'NVTEVM')
    tn.write(b'root\n')
    tn.read_unti1(b'NVTEVM')
    print('Connection established...')

    if choice == 1: # disable
        tn.write(b'mv /mnt/app/res/voice/public/bootsound.raw /mnt/app/res/voice/public/bootsound.raw.bak\n')
    elif choice == 2: # enable
        tn.write(b'mv /mnt/app/res/voice/public/bootsound.raw.bak /mnt/app/res/voice/public/bootsound.raw\n')
    time.sleep(2) # allow time for processing

    tn.write(b'exit\n')
    if choice == 1:
        print('The startup sound was successfully disabled.')
    elif choice == 2:
        print('The startup sound was successfully enabled.')

main()
