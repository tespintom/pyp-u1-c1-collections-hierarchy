# Collections Hierarchy

> **Node**
> A Node is going to be the most basic element of our collections, it represents a single element in the collection. A node has two parameters on instantiation:
> `value`: This contains the value at this element
> `next` *(optional)*: The next element in the collection after this element. If no `next` is provided, it should be set to `None`

### Base Classes

> **Sequenceable**
> Sequenceable collections are well... *sequenceable*. They have both a `start` and an `end` and you can process all the items in between *in sequence*. They also provide a `get_elements()` method to retrieve all the elements of the collection.
> `start`: This should be the first `Node` in the sequence
> `end`: This should be the last `Node` in the sequence
> `get_elements()`: returns a list containing all the **values** of the `Node`s in the collection **in order**.


----------


> **Appendable**
> Collections that are appendable provide the `append(element)` method which adds an element *to the end* of the sequence. This method should update the `start` and `end` if necessary.


----------


> **Popable**
> Popable collections provide the `pop()` method which removes the last element from a sequence and returns it. This method must also update `start`/`end` as necessary.


----------


> **Pushable**
> Pushable collections provide the `push(element)` method which adds a `Node` to the beginning of the sequence, updating `start`/`end` when necessary.


## Running Tests

```bash
# Default. Verbose if too many tests failing
$ py.test tests.py
```

**List tests with -v**

![image](https://user-images.githubusercontent.com/872296/28042585-ea2cabe4-659b-11e7-977f-bc456cb02b37.png)

```bash
$ py.test -v tests.py
```


**Control traceback with --tb**

![image](https://user-images.githubusercontent.com/872296/28042642-30080974-659c-11e7-83dc-28bbf8fe21bf.png)


```bash
$ py.test -v --tb=short tests.py
```

**Match test by name with the -k argument**

![image](https://user-images.githubusercontent.com/872296/28042671-504cfd0c-659c-11e7-8ab0-c8e9c9b7c84a.png)

```bash
$ py.test -v --tb=short tests.py -k test_sequenceable
```

**Run an individual test with a "hard" reference**

![image](https://user-images.githubusercontent.com/872296/28042725-81a36bde-659c-11e7-874e-f40d13bedebe.png)

```bash
py.test -v --tb=short tests.py::test_sequenceable
```

## Running tests with different Python Versions using Tox

Just run `$ tox` to run your tests for every version defined in `tox.ini`.

**Run for a single python version with -e**

![image](https://user-images.githubusercontent.com/872296/28042792-da65afde-659c-11e7-8a07-f5113ed46005.png)

(General syntax: `tox -e[PYTHON-VERSION]`). Example:

```bash
$ tox -epy27
```
