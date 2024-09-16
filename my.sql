insert into students(sid, sname, college, )values(4, "nitish,/;aamit@gmail.com,"col)

alter table students modify column snamevarchar(255)

insert into students (5, "rahul, "abviiit@gmail.com","itm)

insert into students vlues (),(),()

select * from trains
-- give all the data from the column


select name, sex , surviveds from table

select name as passangename, sex as gender, survived from trains


select name , age + 102 as Current age from ttrain,


select name, 10000 as compensation from trains


select distinct sex from trains


select distinct embarked from trains

select distinct pclass from trains

select distinct pclass, embarked from train


selct * from train wher survived = 0
select * from train where pclass = 3

select * from tain where age>50

select * from train where pclass = 3 and survived = 0

select * from train where afe>10 and age<15
\

select   * from train where age between 10 and 15


select title from movies where genre like 'comedy ' or genet like 'action'


select title.genre from moviw where genre in ("action", "horror, " drama")


select title from movies table where title like "A%"

select title from movies where title like "%man%"



select title from movie where actor like '%khan%' or actor like '%kapoo%'

select title from movies where title like '_____'

update passenger set name = 'rahul'

update passenger set name = 'rohi' where email like '&gmail%

update passenger set  name = 'ankit', email = 'abc@gmail.com' where email like '%yahoo%'

delete from passenger where id = 1


delete from movies where id > 2 and email like '%yahoo%'

delete from passenger where 1

---- function 
-- 


select title, (india_gross - profit) as profit from movie



select title, abs((india_gross - profit)) as profit from movies;


select title, round((runtime/60), 1) as runtime_hours from movies


select tile, ceil(runtime/60) as runtime_hourd from movies


select tile, floor(runtime/60) as runtime_hourd from movies


select upper(title) from movies

select title, concat(actor, '', director ) as crew from movies


select title, length(title ) as length from movies,


select title, Substr(title, 1, 5) as short from movies


select max(budget) from movies


select min(earned) from movies

select sum(india_gross) from movies

select avg(india_gross) from movies

select count(*) from movies

select actor, count(distinct(actor))  as movie_count from mobvies


select title, (world wide - budget) as profit from movies order by profit desc linit 5


select * from movies order by genre, title 