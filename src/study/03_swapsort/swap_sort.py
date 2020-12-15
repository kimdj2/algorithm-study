def main():
  a = 3
  b = 2
  c = 1
  if a > b:
    a,b =swap(a,b)
  if b > c:
    b,c =swap(b,c)
  if a > b:
    a,b =swap(a,b)
  print(f"a:{a} b:{b} c:{c}")

def swap(a :int, b: int):
  t = a
  a = b
  b = t
  return a, b
    
if __name__ == '__main__':
    main()