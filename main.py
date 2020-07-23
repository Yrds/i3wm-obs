#!/usr/bin/env python

import asyncio
import simpleobsws
from i3ipc.aio import Connection
from i3ipc import Event
import config as cfg

loop = asyncio.get_event_loop()
ws = simpleobsws.obsws(host=cfg.host, port=cfg.port, password=cfg.password, loop=loop) # Every possible argument has been passed, but none are required. See lib code for defaults.

async def make_request():
    i3 = await Connection().connect()
    await ws.connect() # Make the connection to OBS-Websocket
    i3.on(Event.WORKSPACE_FOCUS, on_workspace_focus)


async def set_source_visibility(source, visibility):
    data = {'source': source, 'render': visibility}
    result = await ws.call('SetSceneItemRender', data)
    return result

async def on_workspace_focus(self, event):
    if event.current.name in cfg.allowed_workspaces:
        result = await set_source_visibility(cfg.source, True)
    else:
        result = await set_source_visibility(cfg.source, False)

loop.run_until_complete(make_request())
loop.run_forever()
