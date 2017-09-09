#1.1
a = 3
a + 2
#5

#1.2
a = a + 1.0
a
#4.0

#1.3
a = 3
b

#1.4
a = 3
a == 5.0
a
#false

#1.5
b = 10
c = b > 9
c
#true

#1.6
5/2 == 5/2.0
#true

#2
3.0 - 1.0 != 5.0 - 3.0
#False

3 > 4 or (2 < 3 and 9 > 10)
#False

4 > 5 or 3 < 4 and 9 > 8
#true

not(4 > 3 and 100 > 6)
#false

import time
import math
currentTime = time.time()
dayT = math.floor(currentTime/(60*60*24))
hourT = math.floor((currentTime/(60*60))%24)
minuteT = math.floor((currentTime/60)%(60*24))
secondT = math.floor(currentTime%(60*60*24))
print("Days:", dayT, "Hours:", hourT, "minutes:", minuteT, "seconds:", secondT,)
