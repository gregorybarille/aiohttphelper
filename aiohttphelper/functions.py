import asyncio
import aiohttp
from types import SimpleNamespace

def __list_to_namespace(data):
    obj = SimpleNamespace()
    obj.text = data[0]
    obj.status = data[1]
    obj.url = str(data[2])
    return obj

def __transform_results(results):
    new_results = []
    for result in results:
        new_results.append(__list_to_namespace(result))
    if len(new_results) == 1:
        new_results = new_results[0]
    return new_results



async def __fetch(session, call, headers, **kwargs):
    async with session.get(call, headers=headers, **kwargs) as response:
        return await response.text(), response.status, response.url

async def __update(session, call, headers, **kwargs):
    async with session.put(call[0], headers=headers, data=call[1], **kwargs) as response:
        return await response.text(), response.status, response.url
        
async def __create(session, call, headers, **kwargs):
    async with session.post(call[0], headers=headers, data=call[1], **kwargs) as response:
        return await response.text(), response.status, response.url

async def __remove(session, call, headers, **kwargs):
    async with session.get(call, headers=headers, **kwargs) as response:
        return await response.text(), response.status, response.url

async def __async_call(method, calls, headers, **kwargs):
    async with aiohttp.ClientSession(raise_for_status=True) as session:
        if not isinstance(calls, (list, tuple)):
            calls = [calls]
        tasks = [ asyncio.ensure_future(method(session, call, headers, **kwargs)) for call in calls]
        return await asyncio.gather(*tasks)

def get(calls, headers, **kwargs):
    loop = asyncio.get_event_loop()
    results = loop.run_until_complete(__async_call(__fetch, calls, headers, **kwargs))
    results_objects = __transform_results(results)
    return results_objects
            
def put(calls, headers, **kwargs):
    loop = asyncio.get_event_loop()
    results = loop.run_until_complete(__async_call(__update, calls, headers, **kwargs))
    results_objects = __transform_results(results)
    return results_objects

def post(calls, headers, **kwargs):
    loop = asyncio.get_event_loop()
    results = loop.run_until_complete(__async_call(__create, calls, headers, **kwargs))
    results_objects = __transform_results(results)
    return results_objects

def delete(calls, headers, **kwargs):
    loop = asyncio.get_event_loop()
    results = loop.run_until_complete(__async_call(__remove, calls, headers, **kwargs))
    results_objects = __transform_results(results)
    return results_objects