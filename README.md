# aiohttphelper

![PyPI](https://img.shields.io/pypi/v/aiohttphelper)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/aiohttphelper)
![GitHub last commit](https://img.shields.io/github/last-commit/gregorybarille/aiohttphelper)
![license](https://img.shields.io/npm/l/redux-saga-testable)

1. [Context](#Context)
2. [Requirements](#Requirements)
3. [Installation / Dependencies](#nstallation)
4. [Usage](#Usage)
5. [Error Handling](#Error)
6. [References](#References)

## Context
The purpose of this package is to make a simple wrapper for aiohttp/calls in order to use it in my personnal / professional projects.

It will make one or several calls using the same session and coroutines.

## Requirements
[```Python >= 3.6```](https://www.python.org/downloads/)

## Installation / Dependencies

```bash
pip install aiohttphelper
```

The following dependencies will also be installed
```python
aiohttp[speedups]==3.6.2
```
## Usage
First import the module:

``` import aiohttphelper ```

You have 4 functions avilable to you:

```python
aiohttphelper.get(calls, headers, **kwargs)
aiohttphelper.put(calls, headers, **kwargs)
daiohttphelper.post(calls, headers, **kwargs)
aiohttphelper.delete(calls, headers, **kwargs)
```

<b>Calls</b> is a list of the urls to request. In case of put/post you need to provide a tuple (url, data):
```python
aiohttphelper.put((url, data), headers, **kwargs)
````

They all return the same thing:

```python
[response.text(), response.status]
```

As it's build in top of aiohttp **kwargs is used to pass parameters to the request.
Look at the [documentation](https://docs.aiohttp.org/en/stable/) for more details.

:warning: !Be carefull the default timeout for the session is 5 minutes, but you can override it:
``` python
aiohttphelper.get('dummy_url', headers='dummy_headers', timeout="10000")
````

## Error Handling
By default all the calls that does not succed will raise an error:
```python
aiohttp.client_exceptions.ClientResponseError
```
If you want to carry on with the calls even if one fails you need to pass ```raise_for_status=False``` as an argument.
If you do so the result will contain the response text and response status in any successfull request.

## References
[aiohttp documentation](https://docs.aiohttp.org/en/stable/)

[aiohttp Licence](https://github.com/aio-libs/aiohttp/blob/master/LICENSE.txt) Copyright 2013-2020 aiohttp maintainers