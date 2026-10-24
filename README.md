# Uday Super Platform - Enterprise Progressive Discipline, Multi-Tenancy & IAM Backend (Django 5.0+ & DRF)

This backend module powers the Multi-Tenant Architecture, Progressive Discipline Engine, IAM (MFA/2FA), and Hybrid RBAC + ABAC Access Policy Framework for the Uday Super HRMS platform.

## Architecture Highlights
- **Framework:** Python 3.11+ | Django 5.0+ | Django REST Framework (DRF)
- **Multi-Tenancy:** Schema / Row-level tenant isolation via `TenantMiddleware` (`X-Tenant-ID` header or subdomain routing) with tenant-scoped models and managers.
- **Identity & Access Management (IAM):**
  - **MFA & 2FA:** Standard RFC 6238 TOTP Authenticator integration (`otpauth://` QR protocol), 8-character single-use emergency recovery backup codes, and step-up authentication tokens for high-privilege operations.
  - **Authentication:** Djoser + SimpleJWT with active **Token Blacklisting** (`rest_framework_simplejwt.token_blacklist`).
- **Hybrid RBAC + ABAC Security Architecture:**
  - **RBAC (Role-Based Access Control):** `SUPER_ADMIN`, `HR_HEAD`, `GENDER_COMMITTEE`, `SAFETY_OFFICER`, `PLANT_HEAD`, `FLOOR_SUPERVISOR`.
  - **ABAC (Attribute-Based Access Control):** Admin-managed policy rules evaluated against Subject, Resource, Action, and Environmental attributes with priority ranking.
  - **Hierarchical Supervisory Authority:** Graph traversal of organizational reporting trees ensuring supervisors exercise authority strictly over their direct or secondary subordinate associates, with automatic conflict-of-interest anti-retaliation checks.
- **Progressive Discipline Automation (5-Step CoT Engine):**
  - Stage 1: Advice Letter (`DDL/HR/ADV/YYYY/XXXX`) — 48-Hour Response Deadline
  - Stage 2: Warning Letter (`DDL/HR/WARN/YYYY/XXXX`) — 48-Hour Response Deadline (Citing Stage 1 Reference)
  - Stage 3: Show Cause & Suspension (`DDL/HR/SC-SUS/YYYY/XXXX`) — 7-Day Response Deadline (Citing Prior Warning Reference)
- **Shift & Overtime Metrics:** Aggregation matrix tracking Staff vs Worker headcounts, standard working hours, and 12-hour extended overtime violations.

## API Endpoints

| Endpoint | Method | Description |
| :--- | :--- | :--- |
| `/api/auth/jwt/create/` | `POST` | Authenticate and obtain JWT access & refresh tokens |
| `/api/tenancy/tenants/` | `GET`, `POST` | Multi-tenant organization registry and configuration |
| `/api/iam/mfa/status/` | `GET` | Current user's 2FA status, backup codes count & step-up state |
| `/api/iam/mfa/setup/` | `POST` | Generate new TOTP secret & QR code uri |
| `/api/iam/mfa/verify/` | `POST` | Verify 6-digit TOTP code and activate 2FA with backup keys |
| `/api/iam/mfa/step-up/` | `POST` | Step-up validation for high-risk operations (e.g. Show Cause) |
| `/api/iam/policies/` | `GET`, `POST` | Admin-managed RBAC + ABAC policy rules |
| `/api/iam/policies/{id}/toggle/` | `POST` | Enable or disable policy rule in real-time |
| `/api/iam/policies/simulate/` | `POST` | Interactive dry-run PolicyEngine with diagnostic trace |
| `/api/iam/hierarchy/` | `GET` | Organizational reporting tree and line authority chain |
| `/api/discipline/actions/` | `GET`, `POST` | Progressive discipline actions with 5-step CoT reasoning |
| `/api/discipline/actions/summary/` | `GET` | High-level compliance stats across stages |
