# Header Injector
-------------------
Header Injector is a tool that checks the target has a "Host Header Injection Vulnerability" or "Host Header based XSS".

# Tested header list

- Host
- X-Host
- X-Forwarded-Host
- X-Forwarded-Server
- X-HTTP-Host-Override
- Forwarded

# Usage

-h or --Help for usage
-f or --File domains.txt for test list of domains

Example: python3 headerInjector.py -f domains.txt
