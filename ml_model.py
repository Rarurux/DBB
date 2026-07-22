def detect_incident(data: dict) -> dict:
    """
    Takes live telemetry data and returns prediction results.
    Checks all anomaly categories independently and reports
    every incident detected, not just the first match.
    """
    cpu = data.get("cpu_usage", 0)
    ram = data.get("ram_usage", 0)
    tx_amount = data.get("amount", 0)

    anomalies = []

    # IT Crash Prediction Logic
    if ram > 85 or cpu > 90:
        anomalies.append({
            "category": "IT_INFRASTRUCTURE",
            "message": "High risk of server; Resource overload detected.",
            "recommended_action": "RESTART_SERVICE"
        })

    # Financial Fraud Detection Logic
    if tx_amount > 9000:
        anomalies.append({
            "category": "FINANCIAL_RISK",
            "message": "Unusual high-value transaction detected.",
            "recommended_action": "FREEZE_ACCOUNT"
        })

    if not anomalies:
        return {
            "is_anomaly": False,
            "category": "NORMAL",
            "message": "Systems nominal.",
            "recommended_action": "NONE"
        }

    return {
        "is_anomaly": True,
        "incident_count": len(anomalies),
        "incidents": anomalies,
        # kept for backward compatibility with any code expecting a single
        # top-level category/message/action
        "category": anomalies[0]["category"],
        "message": anomalies[0]["message"],
        "recommended_action": anomalies[0]["recommended_action"]
    }
