# SQL Filters — Examples and Explanations

This folder contains example SQL queries used during a security investigation to filter records in `log_in_attempts` and `employees` tables. The queries demonstrate use of `AND`, `OR`, `NOT`, and pattern matching with `LIKE` and `%`.

Files:
- `queries.sql`: runnable SQL examples.

Queries and explanations:

- Retrieve After Hours Failed Login Attempts

  SELECT *
  FROM log_in_attempts
  WHERE login_time > '18:00' AND success = 0;

  Explanation: Filters for attempts after 18:00 and where `success = 0` (failed).

- Retrieve Login Attempts on Specific Dates

  SELECT *
  FROM log_in_attempts
  WHERE login_date = '2022-05-09' OR login_date = '2022-05-08';

  Explanation: Uses `OR` to include attempts from either date.

- Retrieve Login Attempts Outside of Mexico

  SELECT *
  FROM log_in_attempts
  WHERE NOT country LIKE 'MEX%';

  Explanation: Excludes rows where `country` starts with `MEX` (e.g., `MEX`, `MEXICO`).

- Retrieve Employees in Marketing (East building)

  SELECT *
  FROM employees
  WHERE department = 'Marketing' AND office LIKE 'East%';

  Explanation: Combines department equality with `LIKE` to match offices in the East building.

- Retrieve Employees in Finance or Sales

  SELECT *
  FROM employees
  WHERE department = 'Finance' OR department = 'Sales';

  Explanation: `OR` returns rows matching either department.

- Retrieve All Employees Not in IT

  SELECT *
  FROM employees
  WHERE NOT department = 'Information Technology';

  Explanation: Excludes employees in the Information Technology department.

Usage

- Copy `queries.sql` into your SQL client and run against your database.
- Adjust table/column names or date/time formats to match your schema.
