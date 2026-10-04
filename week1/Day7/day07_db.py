# Build: A db.py module you’ll reuse for the rest of the roadmap. What it should do: Functions:
# save_message(conversation_id, role, content) and get_messages(conversation_id) using asyncpg , with
# proper error handling (Day 3 skills) if the conversation doesn’t exist.

import asyncio
import asyncpg


    

async def save_message(conn,conversation_id,role,content):

    
    existing_id= await conn.fetchrow(
        "select id from conversations WHERE id =$1", conversation_id
    )
   
    if existing_id is None:
        return "Error: conversation does not exist" 
    else:
        await conn.execute(
        """Insert into message(conversation_id,role,content) values ($1,$2,$3)""",
        conversation_id,
        role,
        content,
    )
    return "save successfully"

async def get_messages(conn,conversation_id):
    existing_id= await conn.fetchrow(
            "select id from conversations WHERE id =$1", conversation_id
        )
    if existing_id is None:
            return "Error: conversation does not exist" 
    else:
        msg=await conn.fetch(
            "Select * from message where conversation_id=$1 order by created_at desc",conversation_id
    )
    return msg
     
async def main():
        conn=await asyncpg.connect(
            user="postgres",
            database="postgres",
            host="localhost",
            port="5432",
            password="uk#postgreysql",
        )
        result=await save_message(conn,1,"assistant","testing")
        print(result)
        convo=await get_messages(conn,2)
        print(convo)
        await conn.close()

    
        
asyncio.run(main())  

