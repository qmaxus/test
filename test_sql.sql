-- TEST 1
select dateop
  from (select dateop, lag(dateop) over (order by dateop) pr_date
          from new_tab) a
 where dateop >= today
   and dateop between pr_date+2 and pr_date+7
 limit 100




 -- TEST 2

select id, name, sales_c, row_number() over (order by sales_c) sales_rank_c, sales_s, row_number() over (order by sales_s) sales_rank_s
  from (select a.id, a.name, count(*) sales_c, sum(b.price) sales_s
          from employee a inner join sales b on a.id = b.employee_id
         group by a.id, a.name)



 -- TEST 3

select
	acc ,
	dt_from,
	LEAD(dt_from,1,'01.01.3000') OVER (Partition BY acc ORDER BY acc, dt_from) AS dt_to,
	SUM(total) OVER (Partition BY acc ORDER BY acc, dt_from) AS balance
from(
	SELECT
		CASE a WHEN 1 THEN "from" ELSE "to" END  acc,
		tdate dt_from ,
		CASE a WHEN 1 THEN -amount ELSE amount END   as total
	FROM transfers, (SELECT 1 a UNION ALL SELECT 2) B
) a;

