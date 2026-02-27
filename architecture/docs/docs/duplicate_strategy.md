# Duplicate Prevention Strategy

## Overview

Duplicate notifications can reduce customer trust and increase annoyance.  
The system implements multiple layers of duplicate prevention.

---

## 1. Hash-Based Deduplication

A unique hash is generated using:

hash(customer_id + event_type + date)

If the same hash already exists in the system within a defined time window, the notification is suppressed.

---

## 2. Time-Window Suppression

The system prevents sending the same type of notification to a customer within a 24-hour window.

Example:
If a "service_due" alert was sent today, it will not be sent again within 24 hours.

---

## 3. Idempotency Keys

Each notification request includes a unique request ID.

If the same request is accidentally processed again, it will not create duplicate notifications.

---

## 4. Notification History Check

Before dispatching a notification, the system checks:

- Last sent timestamp
- Notification status
- Channel used

If already delivered successfully, duplicate sending is avoided.

---

## Result

This multi-layer strategy ensures:

- No repeated alerts
- No double-processing
- Better customer experience
