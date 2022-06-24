a = 10

for b in range(10, -10, -1):
  try:
    res = a/b
    print(a,"/",b,", Result: ", res)
  except Exception as ex:
    print(repr(ex))



x = -1
try:
  if x < 0:
    raise Exception("Sorry, no numbers below zero")
except(BaseException) as e:
  print(repr(e))


print('The End, ', x)
