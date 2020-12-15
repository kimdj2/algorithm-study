def main():
  a = [5,3,2,1,4]
  mini = 0 
  for i in range(len(a)):
    if a[i] < a[mini]:
      mini = i

  print(mini)


if __name__ == '__main__':
    main()