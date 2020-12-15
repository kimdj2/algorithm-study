def main():
  a = [1,3,6,7,10,13,14,17,19,20]
  print(binary_search(a, 19))

def binary_search(a, key):
  left = 0
  right = len(a)

  while left < right:
    mid = (left + right) // 2
    if a[mid] == key:
      return mid
    elif a[mid] < key:
      left = mid + 1
    else:
      right = mid

  return None
if __name__ == '__main__':
    main()