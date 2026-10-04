
# BFS Digital Banking – Risk Matrix

## 1. Purpose

The purpose of this risk matrix is to prioritize testing based on business impact.

Testing effort is not distributed equally across all features.

Higher-risk functionality receives deeper testing, greater automation coverage and stronger release controls.

---

# 2. Risk Classification

| Risk Level | Meaning | Testing Approach |
|---|---|---|
| Critical | Major financial/security/customer impact | Maximum coverage |
| High | Significant business/data impact | Extensive testing |
| Medium | Moderate business impact | Standard testing |
| Low | Limited business impact | Basic validation |

---

# 3. BFS Risk Matrix

| Feature | Business Risk | Impact | Likelihood | Risk | Priority |
|---|---|---|---|---|---|
| Money Transfer | Financial loss | Very High | Medium | Critical | P0 |
| Authentication | Unauthorized access | Very High | Medium | Critical | P0 |
| Account Balance | Incorrect financial data | High | Medium | High | P1 |
| Transaction History | Data integrity | High | Medium | High | P1 |
| Account Information | Customer data issue | High | Low | High | P1 |
| Notifications | Customer communication issue | Medium | Medium | Medium | P2 |
| UI Formatting | Cosmetic issue | Low | Medium | Low | P3 |

---

# 4. Critical Risk Areas

## Money Transfer

Potential risks:

- Incorrect amount
- Duplicate transaction
- Incorrect sender balance
- Incorrect receiver balance
- Partial transaction
- Transaction failure

Testing priority:

**P0 – Critical**

---

## Authentication

Potential risks:

- Unauthorized access
- Invalid credentials accepted
- Session issues
- Access control failure

Testing priority:

**P0 – Critical**

---

## Account Balance

Potential risks:

- Incorrect balance
- Incorrect calculation
- Stale data
- Data synchronization issues

Testing priority:

**P1 – High**

---

## Transaction History

Potential risks:

- Missing transaction
- Duplicate transaction
- Incorrect amount
- Incorrect transaction status

Testing priority:

**P1 – High**

---

# 5. Risk-Based Test Allocation

```text
CRITICAL
   ↓
Maximum Testing
Automation
Negative Testing
Security
Regression
Release Gate

HIGH
   ↓
Extensive Functional Testing
Automation
Regression

MEDIUM
   ↓
Standard Functional Testing
Selective Automation

LOW
   ↓
Basic Validation