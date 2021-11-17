from dudeBro import *

TOTAL = 5


def main():
    print("NFT Generator Started")



iteration = 1
while(iteration < TOTAL):
    # Generate DudeBros
    myDudeBro = DudeBro(iteration)
    iteration = iteration + 1


if __name__ == "__main__":
    main()