import asyncio
import aiohttp

async def __fetch(session, call, headers, **kwargs):
    async with session.get(call, headers=headers, **kwargs) as response:
        return await response.text(), response.status

async def __update(session, call, headers, **kwargs):
    async with session.put(call[0], headers=headers, data=call[1], **kwargs) as response:
        return await response.text(), response.status
        
async def __create(session, call, headers, **kwargs):
    async with session.post(call[0], headers=headers, data=call[1], **kwargs) as response:
        return await response.text(), response.status

async def __remove(session, call, headers, **kwargs):
    async with session.get(call, headers=headers, **kwargs) as response:
        return await response.text(), response.status

async def __async_call(method, calls, headers, **kwargs):
    async with aiohttp.ClientSession(raise_for_status=True) as session:
        if not isinstance(calls, (list, tuple)):
            calls = [calls]
        tasks = [ asyncio.ensure_future(method(session, call, headers, **kwargs)) for call in calls]
        return await asyncio.gather(*tasks)

def get(calls, headers, **kwargs):
    loop = asyncio.get_event_loop()
    return loop.run_until_complete(__async_call(__fetch, calls, headers, **kwargs))   
            
def put(calls, headers, **kwargs):
    loop = asyncio.get_event_loop()
    return loop.run_until_complete(__async_call(__update, calls, headers, **kwargs))

def post(calls, headers, **kwargs):
    loop = asyncio.get_event_loop()
    return loop.run_until_complete(__async_call(__create, calls, headers, **kwargs))

def delete(calls, headers, **kwargs):
    loop = asyncio.get_event_loop()
    return loop.run_until_complete(__async_call(__remove, calls, headers, **kwargs))