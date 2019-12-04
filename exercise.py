import numpy as np

def convert_and_print(c):
    f = c*1.8 + 32
    if f > 75:
        print('Too hot!')
    else:
        print((c,f))

def primeNumber(x):
    prime = False
    primelist = [x for x in range(2,100) if all(x%y != 0 for y in range(2,x))]
    if x in primelist:
        prime=True
    print(primelist)

def array10x10():
    i = np.zeros((10,10))
    i[1:-1, 1:-1] = 1
    print(i)



def main():
    convert_and_print(50)
    convert_and_print(20)
    primeNumber(5)
    array10x10()
if __name__ == "__main__":
    main()
