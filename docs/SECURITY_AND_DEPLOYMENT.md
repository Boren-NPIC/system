# Security and deployment checklist

- Set a unique random SECRET_KEY (32+ random bytes) in environment variables.
- Set COOKIE_SECURE=true behind HTTPS.
- Use PostgreSQL for shared online deployment; do not use SQLite on ephemeral serverless filesystems.
- Keep ADMIN_PASSWORD private and rotate it after first setup.
- Add rate limiting to login and registration before public launch.
- Add email verification and password reset workflow before production.
- Add CSRF protection appropriate to the deployment architecture.
- Add audit events for admin access, report viewing, and report changes.
- Configure automated encrypted database backups and restore tests.
- Review data retention, employee privacy notice, and access policy.
- Run dependency/security scans and test authorization boundaries.
