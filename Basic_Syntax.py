import tensorflow as tf


#Creating a tensor filed with 10- 4 rows and 4 columns each filled with 10 - Used tf.fill()

Filled=tf.fill([4,4],10)
Filled

#Running a session
with tf.Session() as sess:
    Filled=sess.run(Filled)

print(Filled)

#Making new constants a and b
a=tf.constant(4)
b=tf.constant(10)
with tf.Session() as sess:
    c= sess.run(a+b)
print(c)

#Filling a matrix with 0
my_zeros=tf.zeros((4,4))

#Running the session
with tf.Session() as sess:
    my_zeros=sess.run(my_zeros)
    
print(my_zeros)

##Using Random_Uniform and Rndom_Normal
ran_uniform=tf.random_uniform((4,1),minval=1,maxval=4,dtype="int32")
ran_normal=tf.random_normal((4,1),mean=0,stddev=1)
o=[ran_uniform,ran_normal]

#Use another way to run a session-tf.InteractiveSession()
sess=tf.InteractiveSession()
for i in o:
    print(sess.run(i))
    print("\n")
    
 
#Multiplying Matrices
z=tf.constant([[1,3],
              [2,4]])
    
m=tf.constant([[1,5],
              [2,6]])

k=tf.matmul(z,m)
sess=tf.InteractiveSession()
sess.run(k)
