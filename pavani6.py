def main():
    cnt = 0
    number = int(input(""))
    while (number > 0):
      number = number//10
      cnt = cnt + 1
    print (cnt)

if __name__ == '__main__':
    main()
