from Kymang.config import ADMINS
from Kymang.modules.data import *


async def plernya():
    if 1734774709 not in await cek_seller():
        await add_seller(1734774709)
