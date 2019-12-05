import camera;
import network;

def main():
    c = camera.Camera()
    print("All modules initalized.")
    while(1):
        read = raw_input("Please enter command: ")
        print("Read command: " + read)
        try:
            if read == "readimage":
                c.getImage()
            if read == "end":
                c.exit()
                print("Exiting program")
                break
        except:
            print("Something went wrong")
    
if __name__ == "__main__":
   main();
