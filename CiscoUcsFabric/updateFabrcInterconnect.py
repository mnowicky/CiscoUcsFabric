def update_fabric_interconnect(session, base_url):
    url = f"{base_url}/fabricInterconnect"
    payload = {
        "fabricInterconnect": {
            "id": "A",
            "description": "Updated Fabric Interconnect A",
            "managementIp": "192.168.1.10",
            "fcoeEnabled": True
        }
    }

    response = session.put(url, json=payload)
    if response.status_code == 200:
        print("Fabric Interconnect updated successfully.")
    else:
        print("Failed to update Fabric Interconnect:", response.content)

update_fabric_interconnect(session, base_url)

