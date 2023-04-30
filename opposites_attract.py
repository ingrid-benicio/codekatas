def areTheyInlove (x,y):
    if x  % 2 == 0 and y % 2 != 0 or x % 2 != 0 and y % 2 == 0:
          return True
    
    return False


print(areTheyInlove(1,4))