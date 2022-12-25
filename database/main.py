from tortoise import Tortoise, run_async

async def init():
    await Tortoise.init(
        db_url='sqlite://db.sqlite3',
        modules={'models': ['database.models']}
    )
    await Tortoise.generate_schemas()
    await Tortoise.close_connections()

# run_async(init())