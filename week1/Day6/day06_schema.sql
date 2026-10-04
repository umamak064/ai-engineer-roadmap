create table sytem_users(
id SERIAL primary key,
name TEXT,
email Text,
created_at Timestamp default NOW()
);

create table conversations(
id SERIAL primary key,
user_id int references sytem_users(id),
title text,
created_at Timestamp default now()
);

INSERT INTO sytem_users (name, email) VALUES
('Ali','ali@x.com'),('Sara','sara@x.com'),('Ahmed','ahmed@x.com'),
('Zoya','zoya@x.com'),('Bilal','bilal@x.com');

INSERT INTO conversations (user_id, title, created_at) VALUES
(1,'Chat about SQL', NOW() - interval '2 days'),
(1,'Chat about Python', NOW() - interval '10 days'),
(2,'Chat about AI', NOW() - interval '1 day'),
(2,'Chat about DBs', NOW() - interval '40 days'),
(3,'Chat about Docker', NOW() - interval '5 days');

-- 1. A query selecting all conversations created in the last 30 days.--
select id, title,created_at 
from conversations
where created_at > NOW() - interval '30 days'

--2. A query joining users and conversations to show each user’s conversation titles. --
select sytem_users.name,title
from sytem_users
join conversations on sytem_users.id =conversations.user_id

--3. A query counting how many conversations each user has ( GROUP BY ). --
select sytem_users.name, count(conversations.user_id) as total_convo_count
from sytem_users
join conversations on sytem_users.id =conversations.user_id
group by sytem_users.name

--4. A query showing only users with more than 1 conversation ( HAVING ). 
select sytem_users.name, count(conversations.user_id) as total_convo_count
from sytem_users
join conversations on sytem_users.id =conversations.user_id
group by sytem_users.name
having count(conversations.user_id) >1 

--5. A query for the 3 most recent conversations overall ( ORDER BY + LIMIT ). --
select id, title,created_at 
from conversations
order by created_at desc
limit 3

6. A query using LEFT  JOIN to show ALL users, even ones with zero conversations     
select sytem_users.name,conversations.title
from sytem_users
left join conversations on sytem_users.id=conversations.user_id

--Write ONE query (no subqueries) that returns each user's name, their total conversation count,
--and their most recent conversation date — using only JOIN + GROUP BY. 
--Think about what aggregate function gets you "most recent" the same way COUNT got you "how many."

select sytem_users.name,count(conversations.user_id) as total_convo_count, max(conversations.created_at)
from sytem_users
join conversations on sytem_users.id=conversations.user_id
group by sytem_users.name