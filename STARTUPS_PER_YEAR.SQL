--year 2011 has many startups evolved
SELECT founded_year, COUNT(*) AS startup_count
FROM investments
GROUP BY founded_year
ORDER BY startup_count desc
limit 1;
