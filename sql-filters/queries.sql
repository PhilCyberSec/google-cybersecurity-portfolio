-- SQL Filters for security investigation
-- Queries demonstrating AND, OR, and NOT with LIKE and time/date filters

-- Retrieve After Hours Failed Login Attempts
SELECT *
FROM log_in_attempts
WHERE login_time > '18:00' AND success = 0;

-- Retrieve Login Attempts on Specific Dates
SELECT *
FROM log_in_attempts
WHERE login_date = '2022-05-09' OR login_date = '2022-05-08';

-- Retrieve Login Attempts Outside of Mexico
SELECT *
FROM log_in_attempts
WHERE NOT country LIKE 'MEX%';

-- Retrieve Employees in Marketing (East building)
SELECT *
FROM employees
WHERE department = 'Marketing' AND office LIKE 'East%';

-- Retrieve Employees in Finance or Sales
SELECT *
FROM employees
WHERE department = 'Finance' OR department = 'Sales';

-- Retrieve All Employees Not in IT
SELECT *
FROM employees
WHERE NOT department = 'Information Technology';
