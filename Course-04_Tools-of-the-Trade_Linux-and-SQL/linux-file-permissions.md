# Use Linux Commands to Manage File Permissions

**Author:** [Your Name]  
**Date:** [Date]  
**Environment:** Linux (bash shell)

---

## Project Description

The research team at my organisation needs the correct file and directory permissions set to authorise appropriate users and remove unauthorised access. I examined the existing permissions on the file system, identified discrepancies, and updated permissions to reflect the principle of least privilege.

---

## Check File and Directory Details

I used the following command to list the permissions for all files and directories in the `/home/researcher2/projects` directory, including hidden files:

```bash
ls -la /home/researcher2/projects
```

**Sample Output:**

```
total 32
drwxr-xr-x 3 researcher2 research_team 4096 May  1 12:00 .
drwxr-xr-x 8 researcher2 research_team 4096 May  1 12:00 ..
-rw--w---- 1 researcher2 research_team  46 May  1 12:00 .project_x.txt
drwx--x--- 2 researcher2 research_team 4096 May  1 12:00 drafts
-rw-rw-rw- 1 researcher2 research_team  46 May  1 12:00 project_k.txt
-rw-r----- 1 researcher2 research_team  46 May  1 12:00 project_m.txt
-rw-rw-r-- 1 researcher2 research_team  46 May  1 12:00 project_r.txt
-rw-rw-r-- 1 researcher2 research_team  46 May  1 12:00 project_t.txt
```

---

## Describe the Permissions String

The permissions string is a 10-character string. For example: `-rw-rw-rw-`

| Position | Meaning |
|----------|---------|
| 1 | File type: `-` = file, `d` = directory |
| 2–4 | User (owner) permissions: read (`r`), write (`w`), execute (`x`) |
| 5–7 | Group permissions: read (`r`), write (`w`), execute (`x`) |
| 8–10 | Other permissions: read (`r`), write (`w`), execute (`x`) |

For `project_k.txt` (`-rw-rw-rw-`): The user, group, and other all have read and write access. No execute permissions are set. This is overly permissive and must be corrected.

---

## Change File Permissions

### Remove write access for "other" on project_k.txt

The organisation does not permit **other** users to have write access to any file. I used `chmod` to remove it:

```bash
chmod o-w project_k.txt
```

**Verification:**

```bash
ls -la project_k.txt
# -rw-rw-r-- 1 researcher2 research_team 46 May  1 12:00 project_k.txt
```

---

## Change File Permissions on a Hidden File

The hidden file `.project_x.txt` has been archived and should not be writable by anyone, but should be readable by the user and group.

```bash
chmod u-w,g-w,g+r .project_x.txt
```

**Before:** `-rw--w----`  
**After:** `-r--r-----`

---

## Change Directory Permissions

Only `researcher2` should have access to the `drafts` directory; no group or other access should be permitted.

```bash
chmod g-x drafts
```

**Before:** `drwx--x---`  
**After:** `drwx------`

---

## Summary

| Action | Command Used |
|--------|-------------|
| Remove other write on `project_k.txt` | `chmod o-w project_k.txt` |
| Fix hidden file `.project_x.txt` to read-only | `chmod u-w,g-w,g+r .project_x.txt` |
| Remove group execute on `drafts/` | `chmod g-x drafts` |

By applying the principle of least privilege, I ensured that only authorised users retain the minimum necessary access to each resource.
