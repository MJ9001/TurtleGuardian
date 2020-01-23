#import camera;
import network
import sensors

def main():
    n = network.Network()
    n.start()
 #   c = Camera(n)
    print("All modules initalized.")
    while(1):
        read = input("Please enter command: ")
        print("Read command: " + read)
        try:
#            if read == "readimage":
#                c.getImage()
            if read == "networktest":
                n.test()
            if read == "end":
                #c.exit()
                print("Exiting program")
                break
        except Exception as e:
            print("Something went wrong: " + e)
    
if __name__ == "__main__":
   main()
