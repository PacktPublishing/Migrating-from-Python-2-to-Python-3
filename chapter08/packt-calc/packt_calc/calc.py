from aiohttp import web


def add(op1, op2):
    return op1 + op2


def sub(op1, op2):
    return op1 - op2


async def add_handler(request):
    result = add(int(request.match_info['op1']) ,
                 int(request.match_info['op2']))
    return web.Response(text="{}".format(result))


async def sub_handler(request):
    result = sub(int(request.match_info['op1']),
                 int(request.match_info['op2']))
    return web.Response(text="{}".format(result))


def start_server():
    app = web.Application()
    app.add_routes([web.get('/add/{op1}/{op2}', add)])
    app.add_routes([web.get('/sub/{op1}/{op2}', sub)])
    web.run_app(app)
