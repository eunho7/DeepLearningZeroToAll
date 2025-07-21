import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '1'
import tensorflow as tf

hello = tf.constant("Hello, TensorFlow!")

print(hello.numpy())  # b'Hello, TensorFlow!'

'''
위 코드를 실행하면 앞에 b가 붙는다.
b는 byte string 임을 나타낸다.
'''