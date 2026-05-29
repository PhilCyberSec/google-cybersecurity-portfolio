# Apply Filters to SQL Queries

**Author:** [Your Name]  
**Date:** [Date]  
**Environment:** MariaDB / MySQL (SQL)

---

## Project Description

As a security analyst, I used SQL queries with filters to investigate potential security issues, retrieve employee information for security updates, and analyse login activity. The following examples demonstrate how I applied filters using `WHERE`, `AND`, `OR`, `NOT`, and `LIKE` operators.

---

## Retrieve After-Hours Failed Login Attempts

I needed to investigate failed login attempts after business hours (after 18:00). The following query filters for failed logins (`success = 0`) that occurred after 18:00:

```sql
SELECT *
FROM log_in_attempts
WHERE login_time > '18:00:00'
  AND success = 0;
```

**Explanation:** The `WHERE` clause filters rows where `login_time` is after 18:00 AND `success` equals 0 (i.e., the login failed). This helps narrow the investigation to suspicious after-hours activity.

---

## Retrieve Login Attempts on Specific Dates

A suspicious event occurred on 2022-05-09. I retrieved all login attempts on that date and the day before:

```sql
SELECT *
FROM log_in_attempts
WHERE login_date = '2022-05-09'
   OR login_date = '2022-05-08';
```

**Explanation:** The `OR` operator returns rows matching either date, giving full visibility into activity around the suspicious event.

---

## Retrieve Login Attempts Outside of Mexico

Investigation revealed the suspicious activity did not originate in Mexico. I filtered to exclude Mexico-based logins. The `country` column uses both `MEX` and `MEXICO` as values:

```sql
SELECT *
FROM log_in_attempts
WHERE NOT country LIKE 'MEX%';
```

**Explanation:** `LIKE 'MEX%'` matches any value beginning with `MEX` (covering both `MEX` and `MEXICO`). The `NOT` operator excludes those rows, returning only non-Mexican logins.

---

## Retrieve Employees in Marketing (East Building)

The security team needs to update machines for Marketing employees in the East building:

```sql
SELECT *
FROM employees
WHERE department = 'Marketing'
  AND office LIKE 'East%';
```

**Explanation:** The `AND` operator ensures both conditions are met. `LIKE 'East%'` matches any office code starting with `East` (e.g., `East-170`, `East-320`).

---

## Retrieve Employees in Finance or Sales

Employees in Finance and Sales need a different security update:

```sql
SELECT *
FROM employees
WHERE department = 'Finance'
   OR department = 'Sales';
```

**Explanation:** The `OR` operator returns employees from either department, allowing a single query to target both groups.

---

## Retrieve All Employees Not in IT

A final update is required for all employees except those in Information Technology:

```sql
SELECT *
FROM employees
WHERE NOT department = 'Information Technology';
```

**Explanation:** The `NOT` operator excludes IT employees, returning all other departments.

---

## Summary

| Query Goal | Key Operator(s) Used |
|------------|---------------------|
| After-hours failed logins | `WHERE`, `AND` |
| Logins on specific dates | `WHERE`, `OR` |
| Logins outside Mexico | `NOT`, `LIKE` |
| Marketing employees in East | `AND`, `LIKE` |
| Finance or Sales employees | `OR` |
| Non-IT employees | `NOT` |

These SQL filtering techniques enable a security analyst to efficiently investigate incidents and prepare targeted remediation actions.
