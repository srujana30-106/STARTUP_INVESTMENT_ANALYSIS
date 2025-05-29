SELECT market, 
       COUNT(CASE WHEN venture > 0 THEN 1 END) AS venture_count,
       COUNT(CASE WHEN seed > 0 THEN 1 END) AS seed_count,
       COUNT(CASE WHEN angel > 0 THEN 1 END) AS angel_count
FROM investments
GROUP BY market
ORDER BY venture_count DESC;
