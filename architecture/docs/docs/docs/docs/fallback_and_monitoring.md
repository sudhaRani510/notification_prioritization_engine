# Fallback Mechanisms and Monitoring Plan

## Fallback Mechanisms

To ensure system reliability, fallback strategies are implemented.

---

### 1. ML Model Failure Handling

If the ML service fails or times out:

The system switches to rule-based prioritization.

Example Rule Mapping:

- Service overdue → High
- Payment reminder → High
- Test drive reminder → Medium
- Promotional offer → Low

This ensures critical alerts are never blocked.

---

### 2. Notification Delivery Failure

If SMS delivery fails:

- Retry up to 3 times
- Switch to alternate channel (Email / App notification)
- Log failure for monitoring

---

### 3. API Failure Handling

- Implement timeout control
- Use retry mechanism
- Return graceful error response

---

## Monitoring Plan

To maintain system health, the following metrics are tracked:

### System Metrics

- API response time
- Failure rate
- Retry rate
- Duplicate suppression rate

### Notification Metrics

- Delivery success rate
- Open rate
- Click-through rate
- Engagement score

### ML Performance Metrics

- Prediction accuracy
- Priority distribution
- Model confidence score

---

## Logging and Observability

- All notifications logged with timestamp
- Errors recorded with stack trace
- Dashboard integration possible using tools like Prometheus and Grafana

---

## Outcome

This ensures:

- High system availability
- Intelligent fallback
- Performance visibility
- Business reliability
