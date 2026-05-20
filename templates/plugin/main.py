"""AstrBot Plugin Lifecycle Template

This template demonstrates proper lifecycle management including:
- Background task management in activate()/terminate()
- Async HTTP session handling
- Persistent data saving on shutdown

Copy this file as a starting point for your own plugin.
"""

import asyncio
from typing import Optional

import aiohttp
from astrbot.api import logger
from astrbot.api.event import AstrMessageEvent, filter
from astrbot.api.star import Context, Star, register


@register(
    "my_awesome_plugin",
    "YourName",
    "A short description of your plugin",
    "1.0.0",
    "https://github.com/YourName/astrbot_plugin_my_awesome_plugin",
)
class MyPlugin(Star):
    def __init__(self, context: Context, config: dict = None):
        super().__init__(context)
        self.config = config or {}
        self._cleanup_task: Optional[asyncio.Task] = None
        self._session: Optional[aiohttp.ClientSession] = None

    async def activate(self):
        """Called when the plugin is activated.

        Use this to start background tasks, open connections,
        or initialize resources that must persist across handlers.
        """
        logger.info("MyPlugin activated")
        self._session = aiohttp.ClientSession()
        self._cleanup_task = asyncio.create_task(self._periodic_cleanup())

    async def terminate(self):
        """Called when the plugin is unloaded/stopped.

        MUST clean up ALL resources to prevent memory leaks:
        1. Cancel background tasks
        2. Close network sessions
        3. Save persistent data
        """
        logger.info("MyPlugin terminating, cleaning up resources...")

        # 1. Cancel background tasks
        if self._cleanup_task and not self._cleanup_task.done():
            self._cleanup_task.cancel()
            try:
                await self._cleanup_task
            except asyncio.CancelledError:
                pass
            except Exception as e:
                logger.error(f"Error during cleanup task cancellation: {e}")

        # 2. Close HTTP session
        if self._session and not self._session.closed:
            await self._session.close()

        # 3. Save persistent data
        await self._save_data()

        logger.info("MyPlugin terminated successfully")

    async def _periodic_cleanup(self):
        """Example background task: runs every 30 minutes."""
        try:
            while True:
                await asyncio.sleep(1800)
                # Perform periodic cleanup logic here
                logger.debug("Periodic cleanup tick")
        except asyncio.CancelledError:
            logger.debug("Periodic cleanup task cancelled")
            raise

    async def _save_data(self):
        """Example: save plugin state before shutdown."""
        data_dir = self.context.get_data_dir()
        # Save any persistent state here
        logger.info(f"Plugin data directory: {data_dir}")

    @filter.command("hello")
    async def hello(self, event: AstrMessageEvent):
        """Say hello to demonstrate basic command handling."""
        yield event.plain_result("Hello from MyPlugin! The lifecycle template is working.")
