scan a
scan b 

if a <= c and b <= c:
  push a to left pq
  push b to left pq 
  push c to right pq
  c = pop leftpq

elif a <= c and b >= c:
  push a to left pq
  push b to right pq

elif a >= c and b <= c:
  push a to right pq
  push b to left pq

else a >= c and b >= c:
  push a to right pq
  push b to right pq
  push c to left pq
  c = pop leftpq