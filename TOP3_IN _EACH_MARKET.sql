--top 3 companies in each market
SELECT market,NAME,funding_total_usd::BIGINT AS funding
FROM(SELECT market,name,funding_total_usd,
ROW_NUMbER()OVER (PARTITION  BY market ORDER BY funding_total_usd::BIGINT DESC) AS rank
FROM investments) sub
WHERE rank<=3
ORDER BY market, funding desc;
