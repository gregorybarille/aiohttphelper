# AioCalls

The purpose of this package is to make a simple wrapper for aiohttp/calls in order to use it in my personnal / professional projects.

<b>It will make one or several calls using the same session and coroutines.</b>

You need to import the httpcaller first.

``` import aiohttphelper ```

You have 4 functions avilable to you:

```python
def get(calls, headers, **kwargs)
```
```python
def put(calls, headers, **kwargs)
```
```python
def post(calls, headers, **kwargs)
```
```python
def delete(calls, headers, **kwargs)
```
They all return the same thing

```python
[response.text(), response.status]
```

<b>Calls</b> is a list of the urls to request. In case of put/post you need to provide a tuple (url, data):
```python
def put((url, data), headers, **kwargs)
````

As it's build in top of aiohttp **kwargs is used to pass parameters to the request.
Look at the documentation for more details: https://docs.aiohttp.org/en/stable/

! Be carefull the default timeout is 5 minutes, but you can override it:
``` python
aiohttphelper.get('dummy_url', headers='dummy_headers', timeout="10000")
````

