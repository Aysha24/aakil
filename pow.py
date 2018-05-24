def is_power(n):
  while (n!=1):
    if(n%2!=0):
      return false
      n=n//2
  return true
if (is_power(32)):
  print('yes')
else:
  print('no')
