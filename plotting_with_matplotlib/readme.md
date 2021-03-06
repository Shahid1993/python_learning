### Pylab: What Is It, and Should I Use It?

- John D. Hunter, a neurobiologist, began developing matplotlib around 2003, originally inspired to emulate commands from Mathworks’ MATLAB software.

- pylab is a module within the matplotlib library that was built to mimic MATLAB’s global style. It exists only to bring a number of functions and classes from both NumPy and matplotlib into the namespace, making for an easy transition for former MATLAB users who were not used to needing import statements.

> “[pylab] still exists for historical reasons, but it is highly advised not to use. It pollutes namespaces with functions that will shadow Python built-ins and can lead to hard-to-track bugs. To get IPython integration without imports the use of the %matplotlib magic is preferred.”

- Internally, there are a ton of potentially conflicting imports being masked within the short pylab source. In fact, using `ipython --pylab` (from the terminal/command line) or `%pylab` (from IPython/Jupyter tools) simply calls `from pylab import *` under the hood.

- The bottom line is that **matplotlib has abandoned this convenience module and now explicitly recommends against using pylab**, bringing things more in line with one of Python’s key notions: *explicit is better than implicit*.


### The Matplotlib Object Hierarchy

- One important big-picture matplotlib concept is its object hierarchy. A “hierarchy” here means that there is a tree-like structure of matplotlib objects underlying each plot.

- A `Figure` object is the outermost container for a matplotlib graphic, which can contain multiple `Axes` objects.

- Below the `Axes` in the hierarchy are smaller objects such as tick marks, individual lines, legends, and text boxes. Almost every “element” of a chart is its own manipulable Python object, all the way down to the ticks and labels: