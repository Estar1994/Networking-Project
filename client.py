#Hangman Game using TCP and UDP Protocols and Client, Server

from socket import *
from sys import argv 
import string 
from game import *
import server 

def main():

    #parsing command line arguments
    hostname, serverTCPPort = arg[1], int(arg[2])
    
    if len(argv) != 3 or not argv[2].isdigit():
        print("usage: python client.py <server name> <server port>")
        return 1

    print ("Client is running...")
    print ("Remote host {}, remote TCP Port: {}".format(hostname, serverTCPPort))

    #User's Name 
    username = input("Please enter your name: ")

    #TCP Socket
    serverAddress = ((hostname, serverTCPPort))
    clientSocket = socket(AF_INET, Sock_Stream)

    # Get IP address of server via DNS and print it(optional)
    #print (clientSocket.gethostbyname('localhost'))

    # Connect to the server program
    clientSocket.connect((serverAddress))
    print("Connection Made")

    # Send hello message to the server over TCP connection
    clientSocket.send(gameName.encode())

    # TCP Loop
    while True:
        # Read in from TCP port

        print("Received UDP GAMEPORT port#: ",serverTCPPort)

        # Keep listening if it doesn't receive a gameport message
        # Read the control message from the TCP socket and print its contents
        # Break from loop once needed info is received
        break

    # Create a UDP socket
    clientUDPsocket = socket(AF_INET, SOCK_DGRAM)
    clientUDPsocket.connect(serverAddress)
    end = False # default end flag

    # Game loop
    while True:
        # Prompt
        gameInstrs = input('>')
        clientUDPsocket.send(gameInstrs.encode())
        valid_commands = ['start', 'end', 'guess', 'exit']

        if gameInstrs == 'start':
            print(INSTRUCTIONS)
            print("Word: ")


        elif gameInstrs == 'end':
            print("Thanks for playing the word is: ", argv )
            clientSocket.close()
            clientUDPsocket.close()
            break

        elif gameInstrs == 'exit':
            print("Closing TCP and UDP sockets...")
            byeMsg = 'BYE'
            clientUDPsocket.send(byeMsg.encode())
            clientSocket.close()
            clientUDPsocket.close()
            break

        # UDP loop
        while True:
            # Continuously Read in from UDP port
            GUESS = input('>guess ')
            #clientUDPsocket.send(msgTypes.encode())
            if GUESS > str('     '):
                return 1

            valid_msg_types = ["instr", "stat", "end", "na", "bye"]

            # print message
            # Instruction message should be followed by stat message
            # Break once receiving info and reprompt user
            break
            #end of UDP loop

            # If end message received, end client process
            if end:
                break
                #end of Game loop

                # Close sockets
                print("Closing TCP and UDP sockets...")
                clientsocket.close()
                clientUDPsocket.close()
 ###########################################

if __name__ == "__main__":
  main()