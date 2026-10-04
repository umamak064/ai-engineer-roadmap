import asyncio
import asyncpg

async def get_all_users():
        conn=await asyncpg.connect(
            user="postgres",
            database="postgres",
            host="localhost",
            port="5432",
            password="uk#postgreysql",
        )

        print("connected successfully")

#4. Write an async Python function get_all_users() using asyncpg that connects and returns all rows from users
        rows= await conn.fetch(
                "select *  FROM sytem_users",
        )
      
       
       

        await conn.close()
        return(rows)

print(asyncio.run(get_all_users())      )  
