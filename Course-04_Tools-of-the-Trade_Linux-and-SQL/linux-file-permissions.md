```markdown
# File Permissions in Linux

## Project Description
As a security professional working with a research team at a large organization,
I was tasked with reviewing and managing file system permissions to ensure users
were authorized with appropriate access levels. Using Linux commands, I examined
existing permissions across the projects directory, identified misconfigurations,
and applied the principle of least privilege by modifying permissions to remove
unauthorized access and protect sensitive files and directories.

---

## Check File and Directory Details

To check the permissions set for all files and subdirectories in the projects
directory, including hidden files, I used the following command:

```bash
ls -la /home/researcher2/projects
```

**Output:**
```
total 32
drwxr-xr-x 3 researcher2 research_team 4096 Aug 12 09:00 .
drwxr-xr-x 3 researcher2 research_team 4096 Aug 12 09:00 ..
-rw--w---- 1 researcher2 research_team  46  Aug 12 09:00 .project_x.txt
drwx--x--- 2 researcher2 research_team 4096 Aug 12 09:00 drafts
-rw-rw-rw- 1 researcher2 research_team   46 Aug 12 09:00 project_k.txt
-rw-r--r-- 1 researcher2 research_team   46 Aug 12 09:00 project_m.txt
-rw-rw-r-- 1 researcher2 research_team   46 Aug 12 09:00 project_r.txt
-rw-rw-r-- 1 researcher2 research_team   46 Aug 12 09:00 project_t.txt
```

**Explanation:**
The `ls` command lists directory contents. The `-l` flag displays results in long
format showing permissions, ownership, and file size. The `-a` flag includes hidden
files (files beginning with a dot `.`) that would otherwise not be displayed.

---

## Describe the Permissions String

Using `project_k.txt` as an example:

**Permission string:** `-rw-rw-rw-`

| Character | Position | Meaning |
|---|---|---|
| `-` | 1 | File type: `-` means regular file; `d` would mean directory |
| `r` | 2 | Owner has **read** permission |
| `w` | 3 | Owner has **write** permission |
| `-` | 4 | Owner does **not** have execute permission |
| `r` | 5 | Group has **read** permission |
| `w` | 6 | Group has **write** permission |
| `-` | 7 | Group does **not** have execute permission |
| `r` | 8 | Others have **read** permission |
| `w` | 9 | Others have **write** permission |
| `-` | 10 | Others do **not** have execute permission |

**Summary:** `project_k.txt` is a regular file where the owner and group can read
and write, and others can also read and write — which violates the organization's
policy and must be remediated.

---

## Change File Permissions

The organization does not allow others to have write access to any files.
`project_k.txt` had `-rw-rw-rw-` permissions, meaning others had write access.

I used the following command to remove write permission from others:

```bash
chmod o-w project_k.txt
```

**Verification:**
```bash
ls -la project_k.txt
```

**Output:**
```
-rw-rw-r-- 1 researcher2 research_team 46 Aug 12 09:00 project_k.txt
```

**Explanation:**
`chmod` is the command used to change file permissions. `o-w` specifies that
the **others** (`o`) category should have write (`w`) permission **removed** (`-`).
The permission string changed from `-rw-rw-rw-` to `-rw-rw-r--`, confirming
others can now only read the file but no longer write to it.

---

## Change File Permissions on a Hidden File

`.project_x.txt` is a hidden archived file (indicated by the `.` prefix). The
organization requires that no one has write access to it, but both the user and
group should be able to read it.

The current permissions were `-rw--w----`, meaning the user had read/write and
the group had write only — both incorrect.

I used the following command to set the correct permissions:

```bash
chmod u-w,g-w,g+r .project_x.txt
```

**Verification:**
```bash
ls -la .project_x.txt
```

**Output:**
```
-r--r----- 1 researcher2 research_team 46 Aug 12 09:00 .project_x.txt
```

**Explanation:**
- `u-w` removes write permission from the **user (owner)**
- `g-w` removes write permission from the **group**
- `g+r` adds read permission to the **group**

The result `-r--r-----` means the user and group can read the file but nobody
can write to it, and others have no access at all — matching the organization's
requirements for this archived file.

---

## Change Directory Permissions

The `drafts` directory belongs to `researcher2` and only `researcher2` should
be allowed to access it and its contents. The current permissions were
`drwx--x---`, meaning the group had execute access, which should be removed.

I used the following command:

```bash
chmod g-x drafts
```

**Verification:**
```bash
ls -la
```

**Output:**
```
drwx------ 2 researcher2 research_team 4096 Aug 12 09:00 drafts
```

**Explanation:**
`g-x` removes execute (`x`) permission from the **group**. Execute permission
on a directory controls the ability to enter (access) it. By removing this,
only `researcher2` (the owner) can now access the `drafts` directory and its
contents, enforcing the principle of least privilege.

---

## Summary
In this activity, I used Linux commands to audit and remediate file system
permissions for a research team's project directory. I identified four
permission misconfigurations: `project_k.txt` had unauthorized write access
for others; `.project_x.txt` had incorrect write permissions for both user
and group; and the `drafts` directory was accessible to the group when it
should have been restricted to `researcher2` only. Using `ls -la` to audit
permissions and `chmod` to remediate them, I successfully enforced the
organization's access control policies and applied the principle of least
privilege across all affected files and directories.
```
