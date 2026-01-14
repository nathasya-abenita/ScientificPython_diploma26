
### Running Python Scripts

Python scripts are files with a `.py` extension that you can run from command-line.

Make sure you have activated your conda environment and do:

```
python script_name.py
```

(if you do that on an old system, you might need to specify `python3` instead).

#### Difference Between Python Scripts and Jupyter Notebooks:

The `.py` script is executed all at once, from start to finish. This is how you normally run progrmas.
Jupyter notebooks are run cell by cell, which is useful for experimenting with small code snippets and teaching. *Do not use Jupyter notebooks for "real stuff".*

### An extra thing you need to add to the code when you have a script


In Python, if __name__ == "__main__" is used to check whether a script is being run directly or being imported into another script. Here's why it's important:

```python
def my_function():
    print("Function was called")

if __name__ == "__main__":
    print("Script is running directly")
    my_function()
```

In this example, my_function() is only called when the script is run directly. If this script is imported into another script, the code inside the if __name__ == "__main__" block will not execute, preventing unintended behavior or tests from running in the importing script.


### How to deal with pictures:

You need to add `plt.show()` after the plot code to see the picture. However, if you are running from WSL or on remote, it probably won't work. So, you have to save the pictures instead with

```python
plt.savefig("my_plot.png") 
```

### Timing without Jupyter's "magic":

```python
import time

start_time = time.time()

for i in range(1000000):
    i=i**(1/3)+788

end_time = time.time()
elapsed_time = end_time - start_time
print(f"Elapsed time: {elapsed_time} seconds")
```









 
