import asyncio
import aiosqlite
from pathlib import Path

database = Path(__file__).parent.joinpath("database.sqlite3")


async def insert(id, first_name):
    query = """
    INSERT INTO "main"."accounts" ("id", "first_name", "balance","token") VALUES (?,?,?,?)
    """
    values = (
        id,
        first_name,
        None,
        None,
    )
    async with aiosqlite.connect(database=database) as db:
        await db.execute(query, values)
        await db.commit()


async def update_balance(id, balance):
    query = """
    UPDATE "main"."accounts" SET "balance" = ? WHERE rowid = ?
    """
    values = (balance, id)
    async with aiosqlite.connect(database=database) as db:
        await db.execute(query, values)
        await db.commit()


async def update_token(id, token):
    query = """
    UPDATE "main"."accounts" SET "token" = ? WHERE rowid = ?
    """
    values = (
        token,
        id,
    )
    async with aiosqlite.connect(database=database) as db:
        await db.execute(query, values)
        await db.commit()


async def get_by_id(id):
    query = """
    SELECT * FROM "main"."accounts" WHERE rowid = ?
    """
    values = (id,)
    data = None
    async with aiosqlite.connect(database=database) as db:
        db.row_factory = aiosqlite.Row
        async with db.execute(query, values) as res:
            result = await res.fetchone()
            if not result:
                data = result
            else:
                data = {
                    "id": result["id"],
                    "first_name": result["first_name"],
                    "balance": result["balance"],
                }

            return data


async def get_token(id):
    query = """
    SELECT "token" FROM "main"."accounts" WHERE rowid = ?
    """
    values = (id,)
    async with aiosqlite.connect(database=database) as db:
        db.row_factory = aiosqlite.Row
        async with db.execute(query, values) as res:
            result = await res.fetchone()

            if not result:
                return result
            return result["token"]


async def init():
    query1 = """
DROP TABLE IF EXISTS "accounts";
    """
    query2 = """
CREATE TABLE IF NOT EXISTS "accounts" (
  "id" INTEGER NOT NULL,
  "first_name" TEXT,
  "balance" TEXT,
  "token" TEXT,
  PRIMARY KEY ("id")
);
    """
    query3 = """
PRAGMA foreign_keys = true;
    """
    async with aiosqlite.connect(database=database) as db:
        # await db.execute(query1)
        await db.execute(query2)
        await db.execute(query3)
        await db.commit()


async def test():
    await update_balance(1, 1000000000000)
    await update_token(1, "asjdflaskjflaskjdfklajsflkajsdlkfj")
    result = await get_by_id(2)
    print(result)
    result = await get_token(1)
    print(result)
    await insert(2, "akwokoawak")


asyncio.run(init())
