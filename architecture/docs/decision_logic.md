# Decision Logic – Notification Prioritization Engine

## Overview

The system uses a Hybrid ML + Rule-Based approach to determine notification priority.

The final priority score is calculated using:

Priority Score = (ML Score × 0.6) + (Business Urgency × 0.3) + (Customer Value × 0.1)

---

## ML-Based Scoring

A machine learning model predicts urgency based on:

- Days since last service
- Customer lifetime value
- Past notification engagement rate
- Vehicle age
- Response history

The model outputs a score between 0 and 1.

---

## Business Rule Layer

After ML scoring, business rules are applied:

- Service overdue → High urgency
- Test drive reminder → Medium urgency
- Promotional offer → Low urgency

This ensures critical alerts are never ignored.

---

## Customer Value Adjustment

High-value customers receive slightly higher priority weighting.

---

## Final Classification

If:
Score ≥ 0.75 → High Priority  
0.4 ≤ Score < 0.75 → Medium Priority  
Score < 0.4 → Low Priority

---

## Why Hybrid Approach?

- ML provides intelligence and adaptability.
- Rules provide reliability and control.
- Ensures both automation and business safety.Decision logic documentation will be added here.
