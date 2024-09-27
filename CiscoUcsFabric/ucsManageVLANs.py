def create_vlan(session, base_url, vlan_id, vlan_name):
    url = f"{base_url}/network/vlan"
    payload = {
        "vlanId": vlan_id,
        "name": vlan_name,
        "fabric": "A"
    }

    response = session.post(url, json=payload)
    if response.status_code == 201:
        print(f"VLAN '{vlan_name}' created successfully.")
    else:
        print("Failed to create VLAN:", response.content)

create_vlan(session, base_url, "300", "VLAN300")

