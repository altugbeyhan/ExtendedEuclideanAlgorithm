def EEA(a,b):
  if b==0:
    return (a,1,0)
  else:
    (d_prev, x_prev, y_prev) = EEA(b, a % b)
    (d, x, y) = (d_prev, y_prev, x_prev - (a//b)*y_prev)
    return (d, x, y)
    
print(EEA(81,57)) # output : (3, -7, 10) so gcd(81,57) = 3
