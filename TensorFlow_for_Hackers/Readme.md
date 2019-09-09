## Resource : 

# [TensorFlow Basics](https://medium.com/@curiousily/tensorflow-for-hackers-part-i-basics-2c46bc99c930)

![Your data flowing through a graph in TensorFlow](https://miro.medium.com/max/252/1*SmfhKWHXHVEMg8KqNaj-uw.gif)

> A Tensor is a typed multi-dimensional array. For example, a 4-D array of floating point numbers representing a mini-batch of images with dimensions [batch, height, width, channel].

So, you can think of a tensor as a matrix on steroids — expanded to n more dimensions.


### Installing TensorFlow

```python
pip install tensorflow

# or with gpu support
pip install tensorflow-gpu

tf.__version__
```

### Session

```python
v1 = tf.Variable(0.0)
p1 = tf.placeholder(tf.float32)
new_val = tf.add(v1, c1)
update = tf.assign(v1, new_val)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for _ in range(5):
        sess.run(update, feed_dict={p1: 1.0})
    print(sess.run(v1))
```





## References :

- **Basics**
    - [Getting to Know TensorFlow](https://hackernoon.com/machine-learning-with-tensorflow-8873fdee2b68#.ehj5202b0)
    - [Learning TensorFlow Basics](http://learningtensorflow.com/lesson2/)
    - [Deep Learning with TensorFlow](https://bigdatauniversity.com/courses/deep-learning-tensorflow/)