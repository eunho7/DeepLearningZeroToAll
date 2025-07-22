import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '1'
import tensorflow as tf

def adder_node(a, b):
    return tf.add(a, b)

print(adder_node(3.0, 4.5).numpy())         # 7.5
print(adder_node([1.0, 3.0], [2.0, 4.0]).numpy())  # [3. 7.]