def main():
  a = [1,3,6,7,10,13,14,17,19,20]


  print(reverse(a, 0, 10))

def reverse(a, l, r):
  for i in range(l+(r-1)//2-1):
    j = r - (i-l) -1
    a[i], a[j] = swap(a[i] , a[j])
  return a

def swap(a :int, b: int):
  t = a
  a = b
  b = t
  
  return a, b
if __name__ == '__main__':
    main()