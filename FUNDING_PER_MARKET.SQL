--percentage of total funding for each market
WITH total AS (
    SELECT SUM(funding_total_usd::BIGINT) AS total_funding
    FROM investments
    
)
SELECT market,
       SUM(funding_total_usd::BIGINT) AS market_funding,
       ROUND(100.0 * SUM(funding_total_usd::BIGINT) / total.total_funding, 2) AS percent_of_total
FROM investments, total
GROUP BY market, total.total_funding
ORDER BY market_funding DESC;
