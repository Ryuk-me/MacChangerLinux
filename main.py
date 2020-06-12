import subprocess
import random


def banner():
    print(r"""
        _   _   _     _   _   _   _   _   _   _     _   _   _   _   _
       / \ / \ / \   / \ / \ / \ / \ / \ / \ / \   / \ / \ / \ / \ / \
      ( M | a | c ) ( C | h | a | n | g | e | r ) ( L | i | n | u | x )
       \_/ \_/ \_/   \_/ \_/ \_/ \_/ \_/ \_/ \_/   \_/ \_/ \_/ \_/ \_/
    """)

banner()

interface = input("Enter Interface Name  (Enter command ifconfig in terminal to check):")
my_list = ['a', 'b', 'c', 'd', 'e', 'f',1,2,3,4,5,6,7,8,9,0]

random_mac = f"{random.choice([0])}{random.choice(['a','b','f'])}:{random.choice(my_list)}{random.choice(my_list)}:{random.choice(my_list)}{random.choice(my_list)}:{random.choice(my_list)}{random.choice(my_list)}:{random.choice(my_list)}{random.choice(my_list)}:{random.choice(my_list)}{random.choice(my_list)}"


print("1.Do You want Random Mac (Enter 1): ")
print("2.Do You want Custom Mac (Enter 2): ")
user_choice = int(input("Enter Your Choice : "))


if user_choice == 1:
    print("[+] Changing Mac Address For " + interface +" to "+random_mac)
    subprocess.call("ifconfig "+interface +" down",shell=True)
    subprocess.call("ifconfig "+interface +" hw ether "+random_mac ,shell=True)
    subprocess.call("ifconfig "+interface +" up\n",shell=True)
    subprocess.call("ifconfig",shell=True)

elif user_choice == 2:
    user_mac = input("Enter Mac in XX:XX:XX:XX:XX:XX format : ")
    if len(user_mac ) == 17 :
        print("[+] Changing Mac Address For " + interface +" to "+user_mac)
        subprocess.call("ifconfig "+interface +" down",shell=True)
        subprocess.call("ifconfig "+interface +" hw ether "+user_mac,shell=True)
        subprocess.call("ifconfig "+interface +" up",shell=True)
        subprocess.call("ifconfig",shell=True)
    else:
        print("Please Enter In the format ")

elif user_choice not in [1,2]:
    print("Please choose from the above option Only")
