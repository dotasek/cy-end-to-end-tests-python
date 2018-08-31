# End to End Testing for Cytoscape

These Python tests are meant to be run alongside an installed Cytoscape release or release candidate. They provide basic sanity checking and accompany manual testing.

## Setup

These tests are designed to be compatible with Python 2.4-2.7 and 3.0+.

So far, the the following has to be run to install the necessary Python packages:

```
pip install requests
```

## Developers Notes

Developed in PyCharm with automated checking of Python version compatibility. There are other methods of doing this, but this requires little dependence on installed packages for testers. To set up PyCharm this way, open `Settings` and navigate to `Editor > Inspections`. From the `Inspections` panel, select `Code compatibility inspection` and check all the boxes between 2.4 and 3.0 inclusive. Click `Apply`. Your editor should now warn when your code is no longer compatible with all those versions.



