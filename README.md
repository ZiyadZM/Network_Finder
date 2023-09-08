#                                    Network_Finder

First you can do the same thing by using the "Terminal":
1- Open your terminal 
2- write "iwlist scan" then hit enter


But if you want use Python then this how:

import subprocess >>>> by importing "subprocess" module that help you to interact with the system's shell and execute external commands
n = subprocess.check_output(['iwlist', 'scan']) >>>> in this part calling "check_output" to runs an external command and captures its output
print(n.decode('utf-8')) >>>> last The decode() method is used to convert the binary data (bytes) received from the external command into a Unicode string that can be displayed as text

['iwlist', 'scan']  the 'iwlist' command with the 'scan' which is used to list available Wi-Fi networks 