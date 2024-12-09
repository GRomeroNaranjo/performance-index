# performance-index
The performance index will be a critical point if my partner wants to map out his performance and determine if he has improved. Subsequently, it is important to understand it. Find a mathematical explanation below:  

The “
𝑠 
s
 
 
” will represent the speed difference in relation to the accurate specified. The specified speed is 1.5 seconds. (
𝑠=∣∣1.5−𝑡∣∣
s
=
1
.
5
−
t
 
), in here “
𝑡 
t
 
 
” is the time it took, the absolute value of this is found for the metric difference. This is done five times, and then the average speed is found. The average formula is as follows: 
(∑ 5 𝑥=𝑖𝑥𝑖)÷5
∑
 
x
=
i
 
5
x
i
÷
5
 
. Overall, “
𝑠 
s
 
 
” is calculated 5 times, and then the average of them is calculated as final metric. 

Then the consistency is calculated by measuring how many times the roll was straight, and successful. This does not necessarily mean it portrayed exceptional performance, but that it worked. A “1” is assigned for success, a “0” for unsuccessful. The roll is done five times, and the success value kept in the “
𝑥 
x
 
 
” matrix. Then the average is calculated with 
(∑ 5 𝑥=𝑖𝑥𝑖)÷5
∑
 
x
=
i
 
5
x
i
÷
5
 
. That average represents the c value. 

Then the “A” is calculated through a compilation of criteria. There is the landing, the straightness of the roll, and the technique of the roll. All of these are ranked from 1 – 5. This gives is a matrix called “
𝑥 
x
 
 
”. The average of this matrix is calculated with the following equation: 
(∑ 3 𝑥=𝑖𝑥𝑖)÷3
∑
 
x
=
i
 
3
x
i
÷
3
 
. This is then done five times to get five individual values, which are calculated in parallel to find the average using the following equation: 
(∑ 5 𝑥𝑖𝑥𝑖)÷5
∑
 
x
i
 
5
x
i
÷
5
 
. 

After calculating all these values, they must be scaled to achieve the accurate amount respect to each other. Say “
𝑋 
X
 
 
” is the matrix that represents all three values (
𝑠, 𝑎, 𝑐 
s
,
 
a
,
 
c
 
 
). To calculate each individual value, each number should go through the following equation: 
𝑋𝑠𝑐=𝑋−𝑋𝑚𝑖𝑛𝑋𝑚𝑎𝑥−𝑋𝑚𝑖𝑛
X
s
c
=
X
−
X
m
i
n
X
m
a
x
−
X
m
i
n
 
. This is recognized as Minmax Scaling which is widely used in machine learning. However, I can also have this application too. The Minmax Scaling is done for each individual value, and then it is run through the index equation: 
𝑖𝑛𝑑𝑒𝑥=𝑠+𝑎+𝑐3
i
n
d
e
x
=
s
+
a
+
c
3
 
. (Find a python code which calculates the index in appendix a. 
