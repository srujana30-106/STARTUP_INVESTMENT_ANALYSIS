SELECT ROUND(AVG(DATE_PART('year', first_funding_at::DATE) - founded_year)) AS avg_years_to_first_funding
FROM investments
WHERE founded_year IS NOT NULL AND first_funding_at IS NOT NULL;
