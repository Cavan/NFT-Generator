from dudeBro import *

TOTAL = 20


def main():
    print("NFT Generator Started")
    iteration = 1
    while(iteration < TOTAL):
        # Generate DudeBros
        myDudeBro = DudeBro(iteration)
        iteration = iteration + 1
    print("NFT Generation Has Completed")

if __name__ == "__main__":
    main()