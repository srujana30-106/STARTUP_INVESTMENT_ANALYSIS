--Markets that has decreased their funding
WITH funding_by_year AS (
    SELECT market, founded_year, SUM(funding_total_usd::BIGINT) AS yearly_funding
    FROM investments
    WHERE  market IS NOT NULL AND founded_year IS NOT NULL
    GROUP BY market, founded_year
),
funding_change AS (
    SELECT f1.market, f1.founded_year AS year, 
           f1.yearly_funding, 
           f1.yearly_funding - COALESCE(f2.yearly_funding, 0) AS change
    FROM funding_by_year f1
    LEFT JOIN funding_by_year f2 
      ON f1.market = f2.market AND f1.founded_year = f2.founded_year + 1
)
SELECT * FROM funding_change
WHERE change < 0
ORDER BY change;
