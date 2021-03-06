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

- **[Basics](https://medium.com/@curiousily/tensorflow-for-hackers-part-i-basics-2c46bc99c930)**
    - [Getting to Know TensorFlow](https://hackernoon.com/machine-learning-with-tensorflow-8873fdee2b68#.ehj5202b0)
    - [Learning TensorFlow Basics](http://learningtensorflow.com/lesson2/)
    - [Deep Learning with TensorFlow](https://bigdatauniversity.com/courses/deep-learning-tensorflow/)

- **[Building Sample Neural Network](https://medium.com/@curiousily/tensorflow-for-hackers-part-ii-building-simple-neural-network-2d6779d2f91b)**
    - [Visual Information Theory](https://colah.github.io/posts/2015-09-Visual-Information/)
    - [MNIST classification using TensorFlow](https://github.com/aymericdamien/TensorFlow-Examples/blob/master/notebooks/3_NeuralNetworks/multilayer_perceptron.ipynb) — Use Deep Neural Network to classify handwritten digits
    - [How to choose the number of hidden layers and neurons in NN?](https://stats.stackexchange.com/questions/181/how-to-choose-the-number-of-hidden-layers-and-nodes-in-a-feedforward-neural-netw/1097#1097)
    - [How to handle ordinal data in NN models](https://arxiv.org/abs/0704.1028) — Lots of the variables are ordinal. This paper presents an approach to handling that kind of data in NN models
    - [Simpler way to handle ordinal data in NN models](https://stackoverflow.com/questions/38375401/neural-network-ordinal-classification-for-age)
    - [student-alcohol-consumption-prediction](https://github.com/amanchoudhary/student-alcohol-consumption-prediction)

- **[Building a Cat Detector using Convolutional Neural Networks](https://medium.com/@curiousily/tensorflow-for-hackers-part-iii-convolutional-neural-networks-c077618e590b)**
    - [An Intuitive Explanation of Convolutional Neural Networks](https://ujjwalkarn.me/2016/08/11/intuitive-explanation-convnets/)
    - [CS231n — Convolutional Neural Networks (CNNs / ConvNets)](https://cs231n.github.io/convolutional-networks/)
    - [Cats and dogs and convolutional neural networks](http://www.subsubroutine.com/sub-subroutine/2016/9/30/cats-and-dogs-and-convolutional-neural-networks)
    - [Gradient-based learning applied to document recognition](http://yann.lecun.com/exdb/publis/pdf/lecun-01a.pdf)

- **[Creating a Neural Network from Scratch](https://medium.com/@curiousily/tensorflow-for-hackers-part-iv-neural-network-from-scratch-1a4f504dfa8)**
    - [Biases in NNs?](https://stackoverflow.com/questions/2480650/role-of-bias-in-neural-networks)
    - [L1 and L2 Regularization](http://www.chioka.in/differences-between-l1-and-l2-as-loss-function-and-regularization/)
    - [Learn how to do backprop from the pros](http://yann.lecun.com/exdb/publis/pdf/lecun-98b.pdf)
    - [Backpropagation, Intuitions](https://cs231n.github.io/optimization-2/)