import asyncio
from aiohttp import web
#import websockets

def json_response(f):
    async def helper(document, *args):
        print(document, *args)
        ret = await f(document, *args)
        print(ret)
        return web.json_response(ret)
    return helper

async def handle(loop):
    print('inside handle loop')
    app = web.Application(loop=loop)
    routes = web.RouteTableDef()

    @routes.get('/api/test')
    @json_response
    async def handle_test(*args):
        return {'test': 'ok'}

    print('adding routes and preparing to go inside loop')
    app.router.add_routes(routes)
    def handle_all(*args):
        print('**********', args)
        return {'catched': True}
    app.router.add_route('GET', '/{tail:.*}', handle_all)
    await loop.create_server(app.make_handler(), '0.0.0.0', 8089)

def main():    
    loop = asyncio.get_event_loop()
    loop.run_until_complete(handle(loop))
    print("Server started at port 8089")
    loop.run_forever()
    loop.close()

main()