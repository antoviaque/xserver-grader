xserver-grader
==============

Xserver Test Grader for edX

## Installation

Add 'xqueue' and 'xserver' to your playbook (role and nginx site):

```
diff --git a/playbooks/edx_sandbox.yml b/playbooks/edx_sandbox.yml
index 4e312e1..53a4abe 100644
--- a/playbooks/edx_sandbox.yml
+++ b/playbooks/edx_sandbox.yml
@@ -30,6 +32,7 @@
       - cms
       - lms-preview
       - xqueue
+      - xserver
       - ora
     - edxlocal
     - mongo
@@ -40,4 +43,5 @@
     - elasticsearch
     - forum
     - { role: "xqueue", update_users: True }
+    - xserver
     - ora
```

Add the following variables to your ansible configuration:

```
# Xserver
XSERVER_GRADER_DIR: "{{ xserver_data_dir }}/data/content-test-xserver"
XSERVER_GRADER_SOURCE: "https://github.com/antoviaque/xserver-grader.git"
XSERVER_LOCAL_GIT_IDENTITY: "{{ secure_dir }}/files/git-identity"
```

Then re-run your ansible playbook.

## Adding a Code Response Problem to Studio

Create a new course in Studio with the following course details:

* Organization: edX
* Course number: Open_DemoX
* Course name and course run can be anything you want

(This is to benefit from the default demo queue the ansible configuration xqueue
role creates - if you don't use it, you also also need to create an xqueue named
`edX-Open_DemoX`.)

Then add the contents of `problem.xml` to a blank advanced problem in Studio and
edit it.
