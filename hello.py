import tensorflow.compat.v1 as tf

with tf.Session() as sess:
    hello = tf.constant("Hello World!")
    print(sess.run(hello))