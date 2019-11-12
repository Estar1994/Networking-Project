from socket import *
from sys import argv
from random import *
from game import *
import client

def main():


    # Parse command line args
    if len(argv) != 2:
        print("usage: python3 server.py <word to guess or '-r' for random word>")
        return 1


    print("Server is running...")

    # Create the TCP Socket

    print("Creating TCP socket...")
    serverSocket = socket(AF_INET,SOCK_STREAM)

    # Bind a port to the TCP socket, letting the OS choose the port number
    serverSocket.bind(('', 0))
    print("The following is now binded.")


    # Get the port number of the socket from the OS and print it
    # The port number will be a command-line parameter to the client program
    print("Server is listening on port: ", serverSocket.getsockname()[1])

    # Configure the TCP socket (using listen) to accept a connection request
    serverSocket.listen(5)

    try: # try/except to catch ctrl-c
        while True:
            # Accept the TCP Connection
            print("Waiting for a client...\n")
            connectionSocket, addr = serverSocket.accept()
            print("A new client is connected to the server!\n")

            # TCP loop
            while True:
                # Continuously Read in from TCP port
                connectionSocket.sendall(bytes(1024))
                # Keep listening if it doesn't receive a hello message
                # Extract username handling empty case
                gameName = connectionSocket.recv(1024).decode()
                print("User's Name: ", gameName)

                # Create and bind a UDP socket, letting the OS choose the port number
                print("Creating UDP socket...")
                serverUDPSocket = socket(AF_INET,SOCK_DGRAM)
                serverUDPSocket.bind(('', 0))


                # Add a timeout to the UDP socket so that it stops listening
                # after 2 minutes of inactivity
                serverUDPSocket.settimeout(120)

                # Get the port number assigned by the OS and print to console
                UDPportNumber = serverUDPSocket.getsockname()[1]
                print("UDP socket has port number: ", UDPportNumber)

                # Put the UDP port number in a message and send it to the client using TCP
                print("Sending UDP port number to client using TCP connection...")
                #serverUDPSocket.sendto("UDP Port Number: ", ser)
                # Break from loop once needed info is received
                break

            active = False # game not active by default

            # Game (UDP) loop
            while True:
                try:
                    # receive on UDP port here
                    data1, addr = serverUDPSocket.accept()
                    print("UDP port received")

                except timeout: # catch UDP timeout
                    print("Ending game due to timeout...")

                    # break and wait to accept another client
                    break

            if ...:
                #Game setup
                active = True
                word, word_blanks, attempts, win = gameSetup(argv)
                print("Hidden Word: {}".format(word))
                print("Starting game...")
                gameInstrs = data1.receive(1024).decode()
                print(gameInstrs)
                #Send inst then stat messages

            elif ...:
                word_blanks, attempts, win = checkGuess(word, word_blanks, attempts, guess, win)
                guessing = GUESS.recv(1024).decode()
                print(Guess)

                #Losing conditions - break if end
                if len(guess) > 1 and not win or attempts == 0 or win:
                    #Handle win/lose conditions
                    print("Thank you for Playing!")
                    active = False
                else:

            # always send a response message to the client

            # end of UDP Game loop
                        # close the TCP socket the client was using as well as the udp socket.
                    connectionSocket.close()
                    connectionUDPSocket.close()
            # end of TCP loop
                break
    except KeyboardInterrupt:
        # Close sockets
        print("Closing TCP and UDP sockets...")
        connectionSocket.close()
        connectionUDPSocket.close()
###########################################

if __name__ == "__main__":
    main()