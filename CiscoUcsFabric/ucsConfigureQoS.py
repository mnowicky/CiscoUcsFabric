def configure_qos_policy(session, base_url, policy_name):
    url = f"{base_url}/qos-policy"
    payload = {
        "name": policy_name,
        "priority": "high"
    }

    response = session.post(url, json=payload)
    if response.status_code == 201:
        print(f"QoS Policy '{policy_name}' created successfully.")
    else:
        print("Failed to create QoS Policy:", response.content)

configure_qos_policy(session, base_url, "CriticalTraffic")

