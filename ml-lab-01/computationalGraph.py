import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '1'
import tensorflow as tf

node1 = tf.constant(3.0,tf.float32) 
node2 = tf.constant(4.0) # Also tf.float32 implicitly
node3 = tf.add(node1, node2) # node3 = node1 + node2

print("node1:",node1," node2:",node2);
print("node3:", node3)

print("node1, node2: ", node1.numpy(), node2.numpy())
print("node3: ", node3.numpy())
