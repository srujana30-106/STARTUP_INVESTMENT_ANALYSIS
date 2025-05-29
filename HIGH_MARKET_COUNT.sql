select market, count(*) as count
from investments
group by market
order by count desc
limit 5;