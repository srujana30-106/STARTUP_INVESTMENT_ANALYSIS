SELECT 'seed' AS round_type, COUNT(*) FROM investments WHERE seed > 0
UNION 
SELECT 'venture', COUNT(*) FROM investments WHERE venture > 0
UNION 
SELECT 'angel', COUNT(*) FROM investments WHERE angel > 0
UNION 
SELECT 'grant', COUNT(*) FROM investments WHERE grants > 0
UNION 
SELECT 'debt_financing', COUNT(*) FROM investments WHERE debt_financing > 0
ORDER BY COUNT DESC;
