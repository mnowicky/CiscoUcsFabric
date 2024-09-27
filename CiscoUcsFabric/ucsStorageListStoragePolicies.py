def list_storage_policies(session, base_url):
    url = f"{base_url}/storage-policy"
    response = session.get(url)

    if response.status_code == 200:
        policies = response.json()
        print("Storage Policies:")
        for policy in policies['storagePolicies']:
            print(f"- {policy['name']}: {policy['description']}")
    else:
        print("Failed to retrieve storage policies:", response.content)

list_storage_policies(session, base_url)

