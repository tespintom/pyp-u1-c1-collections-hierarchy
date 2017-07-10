# Collections Hierarchy

TODO.

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
