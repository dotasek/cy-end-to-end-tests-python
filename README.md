# End to End Testing for Cytoscape

These Python tests are meant to be run alongside an installed Cytoscape release or release candidate. They provide basic sanity checking and accompany manual testing.

## Prerequisites

These tests are designed to be run on a clean system, with no pre-existing Cytoscape. Should a CytoscapeConfiguration directory exist, rename or move it to run cleanly.

1. These tests are designed to be compatible with Python 2.7 and 3.0+. Python may already be installed on your system; if not, download and install Python from https://www.python.org/

2. Once Python has been installed, the following has to be run to install the necessary Python packages:

```
pip install requests
```

3. These tests are designed to be run on a clean system, with no pre-existing Cytoscape. Should a CytoscapeConfiguration directory exist, rename or move it to run cleanly.

## Installation

Download this project zip [here](https://github.com/dotasek/cy-end-to-end-tests-python/archive/master.zip) and unzip its contents, or clone via git.

## Execution

Start Cytoscape, then execute the following from within this projects root directory:

```
cd CyTestSupport
python CytoscapeEndToEndTests.py 
```

Follow the directions and answer any questions when prompted. Occasionally, the Cytoscape window will take focus away from your terminal, so you may have to click on your terminal again to answer questions.

When the script completes, it should finish with an OK status:

```
----------------------------------------------------------------------
Ran 6 tests in 22.721s

OK
```

## Developers Notes

After making any changes, execute unit tests via the following:

```
python CyTestSupportTests
```

This should return with no failed tests.

This project was developed in PyCharm with automated checking of Python version compatibility. There are other methods of doing this, but this requires little dependence on installed packages for testers. To set up PyCharm this way, open `Settings` and navigate to `Editor > Inspections`. From the `Inspections` panel, select `Code compatibility inspection` and check all the boxes between 2.7 and 3.0 inclusive. Click `Apply`. Your editor should now warn when your code is no longer compatible with all those versions.


## Writing Your Own Tests

To write your own automated tests for Cytoscape core or apps, execute the following from within the projects root directory:

```
pip install .
```

This will install the CyTestSupport module on your machine, to be used in your tests.  Now you can create a new Python file (anywhere on your computer) with the following code:

```
# import and create the CyREST helper object
from CyTestSupport import CyCaller
caller = CyCaller()

# Start a new session
caller.delete("/v1/session")

# Assert that there are not networks in the current session
networks = caller.get("/v1/networks")
assert len(networks) == 0, "Should be no networks, but found {}".format(len(networks))
```

And run it like you would any other Python file:

```python my_file.py```

Happy Testing! :)
