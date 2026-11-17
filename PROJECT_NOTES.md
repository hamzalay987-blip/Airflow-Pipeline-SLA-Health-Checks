# Project notes: Airflow Pipeline SLA Health Checks

**Business problem:** Pipeline teams need explainable run-health checks before failures cascade into stale reports.

**Design:** Evaluate recent runs by DAG and publish actionable breach reasons with deterministic thresholds.

**Interview discussion:** Explain schema assumptions, late data/duplicate behavior, controls, expected tradeoffs, and what would change at enterprise scale.

**Suggested next feature:** Add sample-sized integration tests or a docker-compose service when the implementation is ready.
