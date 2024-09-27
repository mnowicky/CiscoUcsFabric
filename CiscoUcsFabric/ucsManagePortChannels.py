def create_port_channel(session, base_url, port_channel_id):
    url = f"{base_url}/network/port-channel"
    payload = {
        "id": port_channel_id,
        "mode": "active",
        "state": "present"
    }

    response = session.post(url, json=payload)
    if response.status_code == 201:
        print(f"Port Channel '{port_channel_id}' created successfully.")
    else:
        print("Failed to create Port Channel:", response.content)

create_port_channel(session, base_url, "10")

